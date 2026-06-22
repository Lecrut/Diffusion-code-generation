class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    NUMBER1 = 10
    NUMBER2 = 20
    calculator_instance = Calculator()
    sum_result = calculator_instance.add(NUMBER1, NUMBER2)
    print(sum_result)