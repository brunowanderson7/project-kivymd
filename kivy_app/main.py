from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class ManagerWindow(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class ConvertWindow(Screen):
    pass

class CelsiusWindow(Screen):
    def clear(self):
        self.ids.text_box.text = ''
        self.ids.answer.text = ''
    
    def free(self, obj):
        self.dialog.dismiss()

    def toFahrenheit(self):
        
        self.dialog = MDDialog(title = 'ERRO', text = 'Operação invalida, tente novamente!', buttons = [MDFlatButton(text = 'OK', on_release = self.free)])

        try:
            temp = float(self.ids.text_box.text)
            temp = temp*1.8 + 32
            self.ids.answer.text = '{:0.1f} ' .format(temp) + 'Graus Fahrenheit'
        except ValueError:
            self.dialog.open()
        

    def toKelvin(self):
        
        self.dialog = MDDialog(title = 'ERRO', text = 'Operação invalida, tente novamente!', buttons = [MDFlatButton(text = 'OK', on_release = self.free)])

        try:
            temp = float(self.ids.text_box.text)
            temp += 273.15
            self.ids.answer.text = '{:0.1f} ' .format(temp) + 'Graus Kelvin'
        except ValueError:
            self.dialog.open()
        

class FahrenheitWindow(Screen):
    def clear(self):
        self.ids.text_box.text = ''
        self.ids.answer.text = ''

    def free(self, obj):
        self.dialog.dismiss()

    def toCelsius(self):
        
        self.dialog = MDDialog(title = 'ERRO', text = 'Operação invalida, tente novamente!', buttons = [MDFlatButton(text = 'OK', on_release = self.free)])

        try:
            temp = float(self.ids.text_box.text)
            temp = (temp - 32) * 5/9
            self.ids.answer.text = '{:0.1f} ' .format(temp) + 'Graus Celsius'
        except ValueError:
            self.dialog.open()

    def toKelvin(self):
        
        self.dialog = MDDialog(title = 'ERRO', text = 'Operação invalida, tente novamente!', buttons = [MDFlatButton(text = 'OK', on_release = self.free)])

        try:
            temp = float(self.ids.text_box.text)
            temp = (temp - 32) * 5/9 + 273.15
            self.ids.answer.text = '{:0.1f} ' .format(temp) + 'Graus Kelvin'
        except ValueError:
            self.dialog.open()

class KelvinWindow(Screen):
    def clear(self):
        self.ids.text_box.text = ''
        self.ids.answer.text = ''
    
    def free(self, obj):
        self.dialog.dismiss()

    def toFahrenheit(self):
        
        self.dialog = MDDialog(title = 'ERRO', text = 'Operação invalida, tente novamente!', buttons = [MDFlatButton(text = 'OK', on_release = self.free)])

        try:
            temp = float(self.ids.text_box.text)
            temp = (temp - 273.15) * 9/5 + 32
            self.ids.answer.text = '{:0.1f} ' .format(temp) + 'Graus Fahrenheit'
        except ValueError:
            self.dialog.open()

    def toCelsius(self):
        
        self.dialog = MDDialog(title = 'ERRO', text = 'Operação invalida, tente novamente!', buttons = [MDFlatButton(text = 'OK', on_release = self.free)])

        try:
            temp = float(self.ids.text_box.text)
            temp -= 273.15
            self.ids.answer.text = '{:0.1f} ' .format(temp) + 'Graus Celsius'
        except ValueError:
            self.dialog.open()

class AboutWindow(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        self.title = "Temperature Convert"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("main.kv")
    
    def close(self):
        self.stop()
    

MyApp().run()