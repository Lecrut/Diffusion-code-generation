class DivisionHandler:
    @staticmethod
    def divide_numbers(dividend=20.5, divisor=4.2):
        try:
            quotient = dividend / divisor
        except ZeroDivisionError:
            return "Cannot divide by zero"
        else:
            return quotient

if __name__ == '__main__':
    result = DivisionHandler.divide_numbers()
    print(result)