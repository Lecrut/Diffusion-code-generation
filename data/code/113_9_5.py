class NumberOperations:
    def __init__(self, base_number):
        self.base_number = base_number

    def subtract_value(self, value_to_subtract):
        return self.base_number - value_to_subtract

if __name__ == '__main__':
    calculator = NumberOperations(1234567890)
    result1 = calculator.subtract_value(987654321)
    result2 = calculator.subtract_value(1000000)
    print(result1, result2)