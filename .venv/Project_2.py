import tkinter as tk
import math
import csv


class Calculator:
    """
    A  calculator GUI application using Tkinter.
    """

    def __init__(self, master: tk.Tk):
        """
        starts the calculator GUI.

        Args:
            master (tk.Tk): The Tkinter root window.
        """
        self.master = master
        self.master.title("Calculator")
        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.create_buttons()

    def create_buttons(self):
        """
        Create buttons for the calculator.
        """
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('(', 1, 3), (')', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3), ('-', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), ('/', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('π', 4, 2), ('^', 4, 3), ('=', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3), ('DEL', 5, 4),
            ('CLEAR', 6, 0), ('1/x', 6, 1), ('x^2', 6, 2), ('!', 6, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.master, text=text, padx=20, pady=20,
                               command=lambda t=text: self.handle_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def handle_button_click(self, value: str):
        """
        Handles the button inputs.

        Args:
            value (str): The value of the clicked button.
        """
        current_text = self.entry.get()

        if value == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.write_to_csv(result, current_text)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == '^':
            self.entry.insert(tk.END, '**')
        elif value == '√':
            try:
                result = math.sqrt(float(current_text))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.write_to_csv(result, f'sqrt({current_text})')
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == 'x^2':
            try:
                result = eval(current_text) ** 2
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.write_to_csv(result, f'({current_text})^2')
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == '1/x':
            try:
                result = 1 / float(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.write_to_csv(result, f'1/({current_text})')
            except ZeroDivisionError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error: cant divide by zero")
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error: Invalid input")
        elif value == 'DEL':
            self.entry.delete(len(current_text) - 1)
        elif value == 'CLEAR':
            self.entry.delete(0, tk.END)
        elif value == 'π':
            self.entry.insert(tk.END, math.pi)
        elif value == '!':
            try:
                result = math.factorial(int(current_text))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.write_to_csv(result, f'{current_text}!')
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error: Factorials only accepts integers")
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value in {'sin', 'cos', 'tan'}:
            try:
                result = getattr(math, value)(float(current_text))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.write_to_csv(result, f'{value}({current_text})')
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, value)

    def write_to_csv(self, result: float, operation: str):
        """
        Writes the calculation result and operation to a CSV file.

        Args:
            result (float): The result of the calculation.
            operation (str): The mathematical operation performed.
        """
        with open("calc.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([result, f'({operation})'])


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
