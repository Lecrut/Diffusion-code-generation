class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calculator_instance = Calculator()
    first_number = 7
    second_number = 12
    sum_result = calculator_instance.add(first_number, second_number)
    print(sum_result)