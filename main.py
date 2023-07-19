from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"        

        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared-Mathematics"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "Crypto Profit Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 100
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "Crypto Profit Calculator"   
                font_size: '20sp'
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 100
                padding: 10, 10
                on_release:
                    app.root.current = "Crypto_Calculator"
                    root.manager.transition.direction = "left" 
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 100
                padding: 10, 10
                text: "Share Crypto Profit Calculator"
                    
            Image:
                source: 'CryptoQRcode.png'
                size_hint_y: None
                height: 800
                width: 800
""")

Builder.load_string("""
<Crypto_Calculator>
    id:Crypto_Calculator
    name:"Crypto_Calculator"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 100
                padding: 10, 10
                text: "Crypto Profit Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 100
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        investment.text = ""
                        Price.text = ""
                        Profit.text = ""
                        list_of_steps.clear_widgets()       
            
            TextInput:
                id: investment
                text: investment.text
                hint_text: "Investment"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 100
                padding: 10
                        
            
            TextInput:
                id: Price
                text: Price.text
                hint_text: "Current Price of Crypto"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 100
                padding: 10
        
            TextInput:
                id: Profit
                text: Profit.text
                hint_text: "Profit Goal"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 100
                padding: 10              
            
            Button:
                id: steps
                text: "Calculate Profit"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 100
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Crypto_Calculator.steps(investment.text + "@" + Price.text + "#" + Profit.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Crypto_Calculator(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Crypto_Calculator, self).__init__(**kwargs)
            
    layouts = []
    def steps(self,entry):
        print()
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
           print(entry)
           at = entry.find("@")
           investment = entry[:at]
           print("Investment = ",investment)
           
           hashtag = entry.find("#")
           Price = entry[1+at:hashtag]
           print("Price = ",Price)
           
           Profit_goal = entry[1+hashtag:]
           print("Profit_goal = ",Profit_goal)
           
           div = float(Profit_goal) / float(investment)
           print("div",div)
           
           # "$" + str('{:2,.2f}'.format())
           if float(Price) < 0.9:
               price_of_crypto_for_goal = str(float(Price)*float(div))
               print("price_of_crypto_for_goal (IF) = ",price_of_crypto_for_goal)
               
               if price_of_crypto_for_goal.find("e") > 0:
                   print("Found e, format correctly")
                   price_of_crypto_for_goal.find("e")
                   print("e at = ",price_of_crypto_for_goal.find("e"))
                   e = price_of_crypto_for_goal.find("e")
                   left_of_e__and_remove_dash_e_dec = price_of_crypto_for_goal[:e].replace(".","")
                   print("left_of_e__and_remove_dash_e_dec",left_of_e__and_remove_dash_e_dec)
                   right_of_e = int(price_of_crypto_for_goal[e+2:]) - 1
                   print("right_of_e",right_of_e)
                   zeros = "0" * right_of_e
                   price_of_crypto_for_goal = "0." + zeros + left_of_e__and_remove_dash_e_dec
                   print("price_of_crypto_for_goal = $",price_of_crypto_for_goal)
                   
               
           else:
               price_of_crypto_for_goal = str('{:2,.2f}'.format(float(div) * float(Price)))
               print("price_of_crypto_for_goal (ELSE) = ",price_of_crypto_for_goal)
               
               
           self.ids.list_of_steps.add_widget(Label(text= "Investment: $" + str('{:2,.2f}'.format(float(investment))) ,font_size = '20sp', size_hint_y= None, height=100))
           self.ids.list_of_steps.add_widget(Label(text= "Crypto: $" +  Price,font_size = '20sp', size_hint_y= None, height=100))
           self.ids.list_of_steps.add_widget(Label(text= "Profit Goal: $" + str('{:2,.2f}'.format(float(Profit_goal))) ,font_size = '20sp', size_hint_y= None, height=100))
           self.ids.list_of_steps.add_widget(Label(text= "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" ,font_size = '20sp', size_hint_y= None, height=100))
           self.ids.list_of_steps.add_widget(Label(text= "Price of Crypto to earn profit goal: $" + price_of_crypto_for_goal ,font_size = '20sp', size_hint_y= None, height=100))
           self.layouts.append(layout)  
           
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
                
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(Crypto_Calculator(name="Crypto_Calculator"))     
sm.current = "Crypto_Calculator"   

class Crypto_Calculator_App(App):
    def __init__(self, **kwargs):
        super(Crypto_Calculator_App, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    
    def build(app):
        return sm

if __name__ == '__main__':
    Crypto_Calculator_App().run()
    
