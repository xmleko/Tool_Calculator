import math
import tkinter as tk
import re
from tkinter import Button
from tkinter import Label

class Calculator:

    def __init__(self):
        self._mainWindow = tk.Tk()
        self._mainWindow.geometry("412x550")
        self._mainWindow.title("Calculator")
        self._mainWindow.configure(background = "#222222")
        self.string_number = ""
        self.pattern = r'[+\-*/]'
        self.create_button()
        self._mainWindow.mainloop()

    def on_click_button(self, value):
        if str(value) in '+-*/' and any(it in self.string_number for it in '+-*/'):
            self.calculate()
            if self.string_number[-1] in '+-*/':
                pass
            else:
                self.string_number += value
            self.refresh_label_result()
        else:
            self.string_number += str(value)
            self.label_result.config(text=self.string_number)

    def inverse_number(self):
        try:
            self.reverse_number = self.label_result.cget("text")
            if float(eval(self.reverse_number)) > 0:
                if self.string_number[0] == "+":
                    self.string_number = self.string_number[1:]
                self.string_number = ''.join(["-", self.string_number])
            else:
                self.string_number = self.string_number[1:]
                self.string_number = ''.join(["+", self.string_number])
        except Exception:
            self.string_number = "Something went wrong.."
            self.refresh_label_result()

        self.refresh_label_result()

    def number_power_two(self):
        try:
            self.power_number = self.label_result.cget("text")
            if any(it in self.power_number for it in '+-*/'):
                self.split_string = re.split(self.pattern, self.string_number)
                self.operator = re.findall(self.pattern, self.power_number)
                self.string_number = ""
                if len(self.operator) == 1:
                    self.split_string[1] = float(self.split_string[1])**2
                    self.string_number = ''.join([str(self.split_string[0]), self.operator[0], str(self.split_string[1])])
                else:
                    self.split_string[2] = float(self.split_string[2])**2
                    self.string_number = ''.join(
                        [self.operator[0], str(self.split_string[1]), self.operator[1], str(self.split_string[2])])
                self.refresh_label_result()
            else:
                self.power_number = float(self.power_number)**2
                self.string_number = str(self.power_number)
                self.refresh_label_result()
        except Exception:
            self.string_number = "Error Too High Number."
            self.refresh_label_result()

    def number_power_three(self):
        try:
            self.power_number = self.label_result.cget("text")
            if any(it in self.power_number for it in '+-*/'):
                self.split_string = re.split(self.pattern, self.string_number)
                self.operator = re.findall(self.pattern, self.power_number)
                self.string_number = ""
                if len(self.operator) == 1:
                    self.split_string[1] = pow(float(self.split_string[1]), 3)
                    self.string_number = ''.join([str(self.split_string[0]), self.operator[0], str(self.split_string[1])])
                else:
                    self.split_string[2] = pow(float(self.split_string[2]), 3)
                    self.string_number = ''.join([self.operator[0], str(self.split_string[1]), self.operator[1], str(self.split_string[2])])
                self.refresh_label_result()
            else:
                self.power_number = pow(float(self.power_number), 3)
                self.string_number = str(self.power_number)
                self.refresh_label_result()
        except Exception:
            self.string_number = "Error Too High Number."
            self.refresh_label_result()

    def percentage(self):
        try:
            self.number_percentage = self.label_result.cget("text")
            self.split_string = re.split(self.pattern, self.string_number)
            self.operator = re.findall(self.pattern, self.number_percentage)
            self.string_number = ""
            self.number_percentage = self.percentages_count(self.split_string[0], self.split_string[1])
            self.string_number = ''.join([str(self.split_string[0]), self.operator[0], str(self.number_percentage)])
            self.refresh_label_result()
        except Exception:
            self.string_number = "Error Too High Number."
            self.refresh_label_result()

    def percentages_count(self, a, b):
        self.result_percentage = (float(a) * float(b)) / 100
        return self.result_percentage

    def sqrt_number(self):
        try:
            self.sqrt_number = self.label_result.cget("text")
            if float(eval(self.sqrt_number)) < 0:
                self.string_number = "You can't square root of negative number."
                self.refresh_label_result()
            elif any(it in self.sqrt_number for it in '+-*/'):
                self.split_string = re.split(self.pattern, self.string_number)
                self.operator = re.findall(self.pattern, self.sqrt_number)
                self.string_number = ""
                if len(self.operator) == 1:
                    self.split_string[1] = math.sqrt(float(self.split_string[1]))
                    self.string_number = ''.join([str(self.split_string[0]), self.operator[0],  str(self.split_string[1])])
                else:
                    self.split_string[2] = math.sqrt(float(self.split_string[2]))
                    self.string_number = ''.join([self.operator[0], str(self.split_string[1]), self.operator[1], str(self.split_string[2])])
                self.refresh_label_result()
            else:
                self.sqrt_number = math.sqrt(float(self.sqrt_number))
                self.string_number = str(self.sqrt_number)
                self.refresh_label_result()
        except ValueError:
            self.string_number = "Error Invalid Input - Try Again."
            self.refresh_label_result()

    def fraction_number(self):
        try:
            self.fraction_number = self.label_result.cget("text")
            if any(it in self.fraction_number for it in '+-*/'):
                self.split_string = re.split(self.pattern, self.string_number)
                self.operator = re.findall(self.pattern, self.fraction_number)
                self.string_number = ""
                if len(self.operator) == 1:
                    self.split_string[1] = 1 / float(self.split_string[1])
                    self.string_number = ''.join([str(self.split_string[0]), self.operator[0],  str(self.split_string[1])])
                else:
                    self.split_string[2] = 1 / float(self.split_string[2])
                    self.string_number = ''.join([self.operator[0], str(self.split_string[1]), self.operator[1], str(self.split_string[2])])
                self.refresh_label_result()
            else:
                self.fraction_number = 1/float(self.fraction_number)
                self.string_number = ''.join(['', str(self.fraction_number)])
                self.refresh_label_result()
        except ZeroDivisionError:
            self.string_number = "Error Division by Zero - Try Again."
            self.refresh_label_result()
        except ValueError:
            self.string_number = "Error Invalid Input - Try Again."
            self.refresh_label_result()


    def delete_number(self):
        self.string_number = self.string_number[:-1]
        self.refresh_label_result()

    def calculate(self):
        try:
            if self.string_number[-1] in '+-*/':
                pass
            else:
                self.label_result.config(text = str(eval(self.string_number)))
                self.current_value = self.label_result.cget("text")
                self.string_number = str(self.current_value)
        except ZeroDivisionError:
            self.string_number = "Error Division by Zero - Try Again."
            self.refresh_label_result()
        except Exception:
            self.string_number = "Error Invalid Input - Try Again."
            self.refresh_label_result()

    def refresh_label_result(self):
        self.label_result.config(text=str(self.string_number))

    def clear_field(self):
        self.string_number = ""
        self.label_result.config(text = "0")

    def create_button(self):
        self.label_result = Label(self._mainWindow, height = 4, width = 35, font = ('Arial', 11), anchor = 'e', text= "0")
        self.label_result.place(x=40, y=115)
        self.button1 = Button(self._mainWindow, height = 3, width = 13, text="+/-", background="#828282", command = self.inverse_number)
        self.button1.place(x=3, y=492)
        self.button2 = Button(self._mainWindow, height = 3, width = 13, text="1/x", background="#535353", command = self.fraction_number)
        self.button2.place(x=3, y=264)
        self.button3 = Button(self._mainWindow, height = 3, width = 13, text="%", background="#535353", command = self.percentage)
        self.button3.place(x=3, y=207)
        self.button4 = Button(self._mainWindow, height = 3, width = 13, text="x²", background="#535353", command = self.number_power_two)
        self.button4.place(x=105, y=264)
        self.button5 = Button(self._mainWindow, height = 3, width = 13, text="x³", background="#535353", command = self.number_power_three)
        self.button5.place(x=105, y=207)
        self.button6 = Button(self._mainWindow, height = 3, width = 13, text="1", background="#828282", command = lambda: self.on_click_button(1))
        self.button6.place(x=3, y=435)
        self.button7 = Button(self._mainWindow, height = 3, width = 13, text="2", background="#828282", command = lambda: self.on_click_button(2))
        self.button7.place(x=105, y=435)
        self.button8 = Button(self._mainWindow, height = 3, width = 13, text="3", background="#828282", command = lambda: self.on_click_button(3))
        self.button8.place(x=207, y=435)
        self.button9 = Button(self._mainWindow, height = 3, width = 13, text="4", background="#828282", command = lambda: self.on_click_button(4))
        self.button9.place(x=3, y=378)
        self.button10 = Button(self._mainWindow, height = 3, width = 13, text="5", background="#828282", command = lambda: self.on_click_button(5))
        self.button10.place(x=105, y=378)
        self.button11 = Button(self._mainWindow, height = 3, width = 13, text="6", background="#828282", command = lambda: self.on_click_button(6))
        self.button11.place(x=207, y=378)
        self.button12 = Button(self._mainWindow, height = 3, width = 13, text="7", background="#828282", command = lambda: self.on_click_button(7))
        self.button12.place(x=3, y=321)
        self.button13 = Button(self._mainWindow, height = 3, width = 13, text="8", background="#828282", command = lambda: self.on_click_button(8))
        self.button13.place(x=105, y=321)
        self.button14 = Button(self._mainWindow, height = 3, width = 13, text="9", background="#828282", command = lambda: self.on_click_button(9))
        self.button14.place(x=207, y=321)
        self.button15 = Button(self._mainWindow, height = 3, width = 13, text="0", background="#828282", command = lambda: self.on_click_button(0))
        self.button15.place(x=105, y=492)
        self.button16 = Button(self._mainWindow, height = 3, width = 13, text=",", background="#828282", command = lambda: self.on_click_button("."))
        self.button16.place(x=207, y=492)
        self.button17 = Button(self._mainWindow, height = 3, width = 13, text="√", background="#535353", command = self.sqrt_number)
        self.button17.place(x=207, y=264)
        self.button18 = Button(self._mainWindow, height = 3, width = 13, text="C", background="#535353", command = self.clear_field)
        self.button18.place(x=207, y=207)
        self.button19 = Button(self._mainWindow, height = 3, width = 13, text="=", background="#535353", command = lambda: self.calculate())
        self.button19.place(x=309, y=492)
        self.button20 = Button(self._mainWindow, height = 3, width = 13, text="+", background="#535353", command = lambda: self.on_click_button("+"))
        self.button20.place(x=309, y=435)
        self.button21 = Button(self._mainWindow, height = 3, width = 13, text="-", background="#535353", command = lambda: self.on_click_button("-"))
        self.button21.place(x=309, y=378)
        self.button22 = Button(self._mainWindow, height = 3, width = 13, text="*", background="#535353", command = lambda: self.on_click_button("*"))
        self.button22.place(x=309, y=321)
        self.button23 = Button(self._mainWindow, height = 3, width = 13, text="/", background="#535353", command = lambda: self.on_click_button("/"))
        self.button23.place(x=309, y=264)
        self.button24 = Button(self._mainWindow, height = 3, width = 13, background="#535353", text="<--", command = self.delete_number)
        self.button24.place(x=309, y=207)



calc = Calculator()