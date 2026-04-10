import flet as ft 

# //declaration des classes des boutons pour le style et la reutilisation
# @ft.control
# class CalcButton(ft.Button):
#     expand: int = 1


# @ft.control
# class DigitButton(CalcButton):
#     bgcolor: ft.Colors = ft.Colors.WHITE_24
#     color: ft.Colors = ft.Colors.WHITE

# @ft.control
# class ActionButton(CalcButton):
#     bgcolor: ft.Colors = ft.Colors.ORANGE
#     color: ft.Colors = ft.Colors.WHITE

# @ft.control
# class ExtraActionButton(CalcButton):
#     bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
#     color: ft.Colors = ft.Colors.BLACK
    
# Dabord cette version avec des boutons ajoutes directement a la page principale

# def main(page: ft.Page):
#     page.title = "Calc App"
#     result = ft.Text(value="0")

#     page.add(
#         result,
#         ft.Button("AC"),
#         ft.Button("+/-"),
#         ft.Button("%"),
#         ft.Button("/"),
#         ft.Button("7"),
#         ft.Button("8"),
#         ft.Button("9"),
#         ft.Button("*"),
#         ft.Button("4"),
#         ft.Button("5"),
#         ft.Button("6"),
#         ft.Button("-"),
#         ft.Button("1"),
#         ft.Button("2"),
#         ft.Button("3"),
#         ft.Button("+"),
#         ft.Button("0"),
#         ft.Button("."),
#         ft.Button("="),
#     )


# Dans cette partie les boutons sont groupes et classes par ligne grace au Row-Controls
# def main(page:ft.Page):
#     page.title = "Calc App"
#     result = ft.Text(value="0")
       
    # page.add(
    #     ft.Row(controls = [result]),
    #     ft.Row(controls = [
    #             ft.Button("AC"),
    #             ft.Button("+/-"),
    #             ft.Button("%"),
    #             ft.Button("/")
    #         ]
    #            ),
    #    ft.Row(
    #         controls=[
    #             ft.Button("7"),
    #             ft.Button("8"),
    #             ft.Button("9"),
    #             ft.Button("*"),
    #         ]
    #     ),
    #     ft.Row(
    #         controls=[
    #             ft.Button("4"),
    #             ft.Button("5"),
    #             ft.Button("6"),
    #             ft.Button("-"),
    #         ]
    #     ),
    #     ft.Row(
    #         controls=[
    #             ft.Button("1"),
    #             ft.Button("2"),
    #             ft.Button("3"),
    #             ft.Button("+"),
    #         ]
    #     ),
    #     ft.Row(
    #         controls=[
    #             ft.Button("0"),
    #             ft.Button("."),
    #             ft.Button("="),
    #         ]
    #     ),
    #          )
    
    
     # Nous ajoutons le style sur le contenneur(Container) 
     # et sur les boutons a partir des classes(composants utilisable)
     

    # page.add(
    #     ft.Container(
    #         width=350,
    #         bgcolor=ft.Colors.BLACK,
    #         border_radius=ft.BorderRadius.all(20),
    #         padding=20,
    #         content=ft.Column(
    #             controls= [
    #                 ft.Row(
    #                 controls=[result],
    #                 alignment=ft.MainAxisAlignment.END,
    #             ),
    #             ft.Row(
    #                 controls=[
    #                     ExtraActionButton(content="AC"),
    #                     ExtraActionButton(content="+/-"),
    #                     ExtraActionButton(content="%"),
    #                     ActionButton(content="/"),
    #                 ]
    #             ),
    #             ft.Row(
    #                 controls=[
    #                     DigitButton(content="7"),
    #                     DigitButton(content="8"),
    #                     DigitButton(content="9"),
    #                     ActionButton(content="*"),
    #                 ]
    #             ),
    #             ft.Row(
    #                 controls=[
    #                     DigitButton(content="4"),
    #                     DigitButton(content="5"),
    #                     DigitButton(content="6"),
    #                     ActionButton(content="-"),
    #                 ]
    #             ),
    #             ft.Row(
    #                 controls=[
    #                     DigitButton(content="1"),
    #                     DigitButton(content="2"),
    #                     DigitButton(content="3"),
    #                     ActionButton(content="+"),
    #                 ]
    #             ),
    #             ft.Row(
    #                 controls=[
    #                     DigitButton(content="0", expand=2),
    #                     DigitButton(content="."),
    #                     ActionButton(content="="),
    #                 ]
    #             ),
    #         ]
        
    #         )
    #     )
    # )

# if __name__ == "__main__":
#     ft.run(main)
    
   
   
#    code complet de la calculatrice fonctionnelle avec les styles et les classes pour les boutons

from dataclasses import field

import flet as ft


@ft.control
class CalcButton(ft.Button):
    expand: int = field(default_factory=lambda: 1)


@ft.control
class DigitButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.BLACK


@ft.control
class CalculatorApp(ft.Container):
    def init(self):
        self.reset()
        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.BorderRadius.all(20)
        self.padding = 20
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[self.result],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Row(
                    controls=[
                        ExtraActionButton(content="AC", on_click=self.button_clicked),
                        ExtraActionButton(content="+/-", on_click=self.button_clicked),
                        ExtraActionButton(content="%", on_click=self.button_clicked),
                        ActionButton(content="/", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="7", on_click=self.button_clicked),
                        DigitButton(content="8", on_click=self.button_clicked),
                        DigitButton(content="9", on_click=self.button_clicked),
                        ActionButton(content="*", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="4", on_click=self.button_clicked),
                        DigitButton(content="5", on_click=self.button_clicked),
                        DigitButton(content="6", on_click=self.button_clicked),
                        ActionButton(content="-", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="1", on_click=self.button_clicked),
                        DigitButton(content="2", on_click=self.button_clicked),
                        DigitButton(content="3", on_click=self.button_clicked),
                        ActionButton(content="+", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(
                            content="0", expand=2, on_click=self.button_clicked
                        ),
                        DigitButton(content=".", on_click=self.button_clicked),
                        ActionButton(content="=", on_click=self.button_clicked),
                    ]
                ),
            ]
        )

    def button_clicked(self, e):
        data = e.control.content
        print(f"Button clicked with data = {data}")
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


ft.run(main)