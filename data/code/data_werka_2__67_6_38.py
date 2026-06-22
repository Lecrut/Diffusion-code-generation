class SumCalculator:
    def __init__(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise ValueError("Both attributes must be numbers.")
        self.value1 = value1
        self.value2 = value2

    def calculate_sum(self):
        return self.value1 + self.value2

if __name__ == '__main__':
    try:
        calculator_instance = SumCalculator(10, 20)
        result = calculator_instance.calculate_sum()
        print(result)
    except ValueError as e:
        print(e)