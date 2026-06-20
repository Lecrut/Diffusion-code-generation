class Divider:
    def divide(self, num1: float, num2: float) -> float:
        try:
            return num1 / num2
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")

if __name__ == '__main__':
    divider = Divider()
    result = divider.divide(20.5, 4.2)
    print(result)