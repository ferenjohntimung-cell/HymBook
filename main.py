from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# App background color
Window.clearcolor = (0.05, 0.05, 0.1, 1)

# Save users
users = {}

# Hymns
hymns = {
    "1. HOSSANA IN THE HIGHEST":
    "Hossanna, Hossanna in the highest (2)\n\nLord, we lift up your name,\n\nWith heart full of praise\n\nBe exalted oh lord my God-\n\nHossanna in the highest.\n\nGlory,Glory,Glory to the king of kings......\n\nJESUS,JESUS,JESUS is the prince of peace.",

    "2. BLESSED BE THE NAME OF THE LORD":
    "Blessed be the name of the lord (2)\nBlessed be the name of the lord most high (rept)\n\n\n(CHORUS)\nThe name of the Lord is the strong tower\nThe righteous run into it\nAnd they save (rpt)\n\n Holy is the name of the Lord......\nGlory to the name of the Lord.......",

    "3. HE IS EXALTED":
    "He is exalted\nThe king is exalted on high;\nI will praise Him\nHe is exalted,forever exalted on high\nAnd I will praise His name!\nHe is the Lord\n\n(CHORUS)\nForever His truth shall reign\nHeaven and earth\nRejoice in His Holy name.\nHe is exalted,the king is exalted on high.(rept)",
    
    "4. LORD I LIFT YOUR NAME ON HIGH":
        "Lord I lift your name on high\nLord I love to sing your praises\nI'm so glad you're in my life\nI'm  so glad you came to save us.\n\n(CHORUS)\nYou came from Heaven to earth to show the way\nFrom the earth to the cross my debt to pay\nFrom the cross to the grave\nFrom the grave to the sky\nLord I lift your name on high.(rept)",
        
        "5. SHOUT TO THE LORD":
            "My Jesus,my Saviour\nLord,there is none like you\nAll of my days I want to praise\nThe wonders of your mighty love\nMy comfort,my strength\nTower of refuge and strength\nLet every breath all that I am\nNever cease to worship you.\n\nShout to the lord\nAll the earth let us sing\nPower and majesty praise to the king\nMountains bow down\nAnd the sea will roar\At the second of your name\nI sing for joy at the work of your hands\nForever I'll love you,forever I stand\nNothing compare to the promise\nI have in you (rept)",
            
            "6. GLORY":
                "Glory,glory in the highest\nGlory,to the almighty;\nGlory to the Lamb of God.\nAnd glory to the living word;\nGlory to the Lamb!\n\nI give glory(glory)glory(glory)\nGlory,glory to the Lamb!\nI give glory,(glory)glory(glory)\nGlory,glory to the Lamb!\nI give  glory to the Lamb!",
                
                "7. THERE IS POWER IN THE NAME OF JESUS":
                    "There is power in the name of Jesus\nWe believe in His name\nWe have called on the name of Jesus;\nWe are saved, we are save!\nIn His name the demons flee.\nAt His name captives are freed.\nFor there is no other name\nThat is higher than Jesus.\n\nThere is power in the name of Jesus\nLike a word in our hands.\nWe declare in the name of Jesus\nWe shall stand!We shall stand!\nAt His name God's enemies!\nShall be crushed beneath our feet\nFor there is no other name\nThat is higher than Jesus name.",
                    
                    "8. I'LL REACH UP HIGH":
                    "I'll reach up high and touch the ground,\nI'll stamp my feet and I'll turn around,\nI've go to praise the Lord.\nI'll jump and dance with all my might;\nI might look funny but that's alright,\nI've got to praise the Lord.\n\nI'll do anything just for my Lord;\n'Cause he's done everything for me,\nIt doesn't matter who is looking on\nJesus is the person that I want to please\nMay my whole life be a song of praise\nTo worship God in every way,\nIn this song the actions praise His name,\nI want my actions praise His name",
                    
                    "9. JESUS,NAME ABOVE ALL NAMES":
                        "Jesus,Name above all Names\nBeautiful saviour,glorious Lord\nEmmanuel,God is with us,\nBlessed redeemer,living word.",
                        
                        "10. DEEP DEEP DOWN IN MY HEART":
                            "Deep deep oh deep down down\nDeep down in my heart (2)\nDo you love my Jesus?\nDeep down in my heart\nYes,I love my Jesus\nDeep down in my heart\n(repeat)",
                            
                            "11. WE WANNA SEE JESUS LIFTED HIGH":
                                "We wanna see Jesus lifted high\nA banner that flies across the land\nThat all man might see the truth and know\nHe is the way to heaven.\n\n(Chorus)\nWe wanna see (3x)\nJesus lifted high\n\nStep by step we're moving forward\nLittle by little we're taking ground\nEvery prayer a powerful weapon\nStrong holds come\nTumbling down and down and down",
                                
                                "12. MERCY IS FALLING":
                                    "Mercy is falling,is falling,is falling\nMercy is falling like a sweet spring rain\nMercy is falling,is falling all over me\n\nHey oh....,I receive your mercy\n Hey oh,I receive your grace\nHey oh,I will dance forevermore.\n(Repeat)",
                                    
            
       "13. I WILL SING OF THE MERCIES":
                                    "I will sing the mercies of the Lord forever;\nI will sing,I will sing.\nI will sing of the mercies of the Lord forever\nI will sing of the mercies of the Lord.\nWith my mouth will I make known\nThy faithfulness,Thy faithfulness\nWith my mouth will I make known\nThy faithfulness to all generations\n(Repeat)",         
                                    
                "14. I FIX MY EYES ON YOU":
                "I fix my eye on you\nThe author of my faith;\nCasting aside every sin and every weight\nI fix my eye on you\nI lay burdened down,letting the cares\nOf this world now fade away.\n\nOne thing I ask,this one thing I seek\nThat I may dwell in your house;\nOh Lord,my king,all the days of my life\nI want gaze upon your beauty\nAnd seek you in this holy place.",
                
                                                                     ""                                                     
                                    
                                    
                                    
                                    
                                    
}

# ---------------- LOGIN SCREEN ---------------- #

class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = FloatLayout()

        # Background
        with root.canvas.before:
            Color(0.06, 0.06, 0.12, 1)
            self.bg = RoundedRectangle(
                size=Window.size,
                pos=(0, 0)
            )

        # Main Login Box
        box = BoxLayout(
            orientation='vertical',
            spacing=18,
            padding=30,
            size_hint=(0.85, 0.78),
            pos_hint={"center_x": 0.5, "center_y": 0.58}
        )

        # Box Design
        with box.canvas.before:
            Color(0.15, 0.15, 0.25, 1)
            self.box_bg = RoundedRectangle(
                size=box.size,
                pos=box.pos,
                radius=[25]
            )

        box.bind(size=self.update_box)
        box.bind(pos=self.update_box)

        # Logo
        logo = Image(
            source="logo.png",
            size_hint=(1, None),
            height=450
        )

        # Title
        title = Label(
            text="MELODY OF FAITH",
            font_size=52,
            bold=True,
            color=(1, 0.8, 0, 1),
            size_hint=(1, None),
            height=55
        )

        # Username
        self.username = TextInput(
            hint_text="Username",
            multiline=False,
            font_size=22,
            size_hint=(1, None),
            height=65,
            padding=[15, 18],
            background_color=(0.2, 0.2, 0.3, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )

        # Password
        self.password = TextInput(
            hint_text="Password",
            multiline=False,
            password=True,
            font_size=22,
            size_hint=(1, None),
            height=65,
            padding=[15, 18],
            background_color=(0.2, 0.2, 0.3, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )

        # Show Password Button
        self.show_btn = Button(
            text="SHOW PASSWORD",
            size_hint=(1, None),
            height=50,
            font_size=16,
            background_normal='',
            background_color=(0.3, 0.3, 0.45, 1)
        )

        self.show_btn.bind(on_press=self.toggle_password)

        # Login Button
        login_btn = Button(
            text="LOGIN",
            font_size=22,
            bold=True,
            size_hint=(1, None),
            height=65,
            background_normal='',
            background_color=(1, 0.7, 0, 1)
        )

        # Register Button
        register_btn = Button(
            text="REGISTER",
            font_size=22,
            bold=True,
            size_hint=(1, None),
            height=65,
            background_normal='',
            background_color=(0.35, 0.35, 0.45, 1)
        )

        login_btn.bind(on_press=self.login)
        register_btn.bind(on_press=self.register)

        # Add Widgets
        box.add_widget(logo)
        box.add_widget(title)
        box.add_widget(self.username)
        box.add_widget(self.password)
        box.add_widget(self.show_btn)
        box.add_widget(login_btn)
        box.add_widget(register_btn)

        root.add_widget(box)

        self.add_widget(root)

    # Update rounded box
    def update_box(self, *args):
        self.box_bg.pos = args[0].pos
        self.box_bg.size = args[0].size

    # Show / Hide Password
    def toggle_password(self, instance):

        self.password.password = not self.password.password

        if self.password.password:
            self.show_btn.text = "SHOW PASSWORD"
        else:
            self.show_btn.text = "HIDE PASSWORD"

    # Register
    def register(self, instance):

        user = self.username.text
        pwd = self.password.text

        if user == "" or pwd == "":
            self.popup("Please enter username and password")
            return

        users[user] = pwd

        self.popup("Registered Successfully")

    # Login
    def login(self, instance):

        user = self.username.text
        pwd = self.password.text

        if user in users and users[user] == pwd:
            self.manager.current = "home"
        else:
            self.popup("Wrong Username or Password")

    # Popup
    def popup(self, text):

        pop = Popup(
            title="Holy Hymnal",
            content=Label(
                text=text,
                font_size=20
            ),
            size_hint=(0.75, 0.35)
        )

        pop.open()

# ---------------- HOME SCREEN ---------------- #

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        # Header
        title = Label(
            text="Hymn Songs",
            font_size=30,
            bold=True,
            color=(1, 0.8, 0, 1),
            size_hint=(1, None),
            height=60
        )

        # Scroll Area
        scroll = ScrollView()

        song_layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            size_hint_y=None,
            padding=10
        )

        song_layout.bind(
            minimum_height=song_layout.setter('height')
        )

        # Add Hymns
        for hymn in hymns:

            btn = Button(
                text=hymn,
                size_hint_y=None,
                height=70,
                font_size=30,
                bold=True,
                background_normal='',
                background_color=(0.2, 0.2, 0.3, 1)
            )

            btn.bind(
                on_press=lambda x, h=hymn:
                self.show_song(h)
            )

            song_layout.add_widget(btn)

        scroll.add_widget(song_layout)

        root.add_widget(title)
        root.add_widget(scroll)

        self.add_widget(root)

    # Show Song Lyrics
    def show_song(self, hymn):

        content = BoxLayout(
            orientation='vertical',
            padding=15,
            spacing=15
            
        )

        lyrics = Label(
            text=hymns[hymn],
            font_size=28
        )

        close_btn = Button(
            text="CLOSE",
            size_hint=(1, None),
            height=50,
            bold=True,
            background_normal='',
            background_color=(1, 0.7, 0, 1)
        )

        content.add_widget(lyrics)
        content.add_widget(close_btn)

        popup = Popup(
            title=hymn,
            content=content,
            size_hint=(0.9, 0.6)
        )

        close_btn.bind(on_press=popup.dismiss)

        popup.open()

# ---------------- APP ---------------- #

class HymnalApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))

        return sm

# Run App
HymnalApp().run()