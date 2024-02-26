from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from tools.Utils import *
from kivymd.app import MDApp



class ZequentNavigationDrawer(MDNavigationDrawer):
    i = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def on_state(self, widget, state):
        if self.i == 0:
            self.app=MDApp.get_running_app()
            navigationItems = Utils.getNavigationDrawerItems(self.app.root.ids.translator, self.app.root.ids.sm)
            
            for item in navigationItems:
                self.ids.drawer_menu.add_widget(item)
            self.i=1
            
                