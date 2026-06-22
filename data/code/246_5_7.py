class Calculator:

    def add(self, a, b):
        try:
            num_a = float(a)
            num_b = float(b)
            return num_a + num_b
        except ValueError:
            raise ValueError('Both inputs must be numeric')
if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(10, 5))
    print(calc.add('12.5', 3.5))