#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:35:34 2021

@author: home
"""


import datetime


from bokeh.models import ColumnDataSource, Panel, Tabs, DataTable, TableColumn
from bokeh.models.widgets import Button, Div
from bokeh.layouts import column, row, Spacer

from bokeh.io import curdoc

#data_table = pd.read_csv('/data_table.csv')

"""
Logo
Title
Instructional Section for left side of Dashboard
"""

#Logo for top corner
logoLoc = "app/static/logo.png" #os.getcwd().split('/')[-1]+
logo = Div(text="<img src= %r >" % logoLoc)

#logo = figure(match_aspect=True)
#logo.image_url( ['file://ebBokehFlask/static/logo.png'], 0, 0, 1, 1)

#Title object, I added some wrappers to help with spacing.
title = Div(text="""Standard Bokeh Dashboard Starter""",
             style={'font-size': '150%', 'color': '#06bac5'},
             sizing_mode = 'fixed',
             align = 'center',
             width = 600,
             height = 25)



#Instruction section writtin in HTML, it might be good to create a instructions object similar to Title for multiple paragraphs.
instructions = Div(text="""Instructions can be written here.
                   Your <a href="https://en.wikipedia.org/wiki/HTML">HTML</a>-supported text is initialized with the <b>text</b> argument.  
                   The remaining div arguments are <b>width</b> and <b>height</b>. 
                   For this example, those values are <i>200</i> and <i>100</i>, respectively.""",
                    sizing_mode = 'fixed',
                    width=290, 
                    height=100)

"""
Initial Data Section
The application needs to have, at least, generic data to propogate first visuals.
"""

#create some data that can be updated easily
timestamp = str(datetime.datetime.now())

#create the column datasource which is the datatype that can be continually updated within Bokeh
#data = {'Timestamp': [timestamp]}
source = ColumnDataSource(data = {'Timestamp': [timestamp]})

"""
Create the main objects that will populate the dashboard 
"""

columns = [TableColumn(field="Timestamp", title="Datetime")]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

"""
Actively Updating Section
"""   
#easy function to create a timestamp      
def gen_timestamp():
    current_timestamp = str(datetime.datetime.now())
    return current_timestamp

#generic data update
def update_datasource():
    current_time = gen_timestamp()
    source.data = {'Timestamp': [current_time]}
  
#action button
update_button = Button(label="Update the Timestamp", width=150)
update_button.on_click(update_datasource)   


"""
Layout and Organization

|-------------|
| @  |--------|
|--| |--------|
|  | |        |
|  | |        |
|  | |--------|
--------------|

Logo  Spacer Top Row
Column  Spacer Dash Column
"""

#generic spacers
wspace_50 = Spacer(min_width = 50) 
hspace_10 = Spacer(min_height = 10) 
wspace_10 = Spacer(min_width = 10) 

#dash_1 is the only thing that realitically will need to change in a large way between projects
dash_1 = column(update_button,data_table)

#Makes the dash section into a tab sorted section
dash_tab1 = Panel(child=dash_1, title="   Main Dashboard   ")
dashboard = Tabs(tabs=[dash_tab1])

#title objects
title_obj = row(wspace_50, title, margin = 25)

#container sections
logo_space= column(logo, height=100, width=300)

#organize the section into the two core columns
column_1 = column(logo_space, hspace_10, row(wspace_10, instructions))

column_2 = column(title_obj, dashboard)

data_app = row(column_1, wspace_50, column_2)


curdoc().add_root(data_app)
curdoc().title = 'Web App Title'



