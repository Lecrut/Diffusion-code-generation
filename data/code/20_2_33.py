class Comparator:

    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    comparator = Comparator()
    value1 = 42
    value2 = 42
    value3 = 'hello'
    value4 = 'world'
    result1 = comparator.check_equality(value1, value2)
    print(f'Are {value1} and {value2} equal? {result1}')
    result2 = comparator.check_equality(value3, value4)
    print(f"Are '{value3}' and '{value4}' equal? {result2}")