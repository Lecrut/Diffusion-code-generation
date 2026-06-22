class Calculator:

    def __init__(self):
        self.attributes = {}

    def add(self, key1, key2):
        try:
            value1 = float(self.attributes.get(key1, 0))
            value2 = float(self.attributes.get(key2, 0))
            return value1 + value2
        except ValueError:
            return 'Error: Invalid input. Please enter numeric values.'

    def set_attribute(self, key, value):
        self.attributes[key] = value
if __name__ == '__main__':
    calc = Calculator()
    calc.set_attribute('a', 10)
    calc.set_attribute('b', 5)
    calc.set_attribute('c', 'hello')
    calc.set_attribute('d', 3.14)
    print(calc.add('a', 'b'))
    print(calc.add('c', 'd'))
    print(calc.add('b', 'd'))