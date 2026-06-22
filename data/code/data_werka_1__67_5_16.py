class Calculator:

    def add(self, a, b):
        try:
            result = float(a) + float(b)
            return result
        except ValueError:
            return 'Error: Non-numeric input'
if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 10))
    print(calc.add('20', '30'))
    print(calc.add('a', 10))