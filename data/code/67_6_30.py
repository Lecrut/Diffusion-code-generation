class SumCalculator:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def calculate_sum(self):
        if not isinstance(self.attribute1, (int, float)) or not isinstance(self.attribute2, (int, float)):
            raise ValueError("Both attributes must be numbers")
        return self.attribute1 + self.attribute2

if __name__ == '__main__':
    try:
        calculator = SumCalculator(4.5, 6)
        result = calculator.calculate_sum()
        print(result)
    except ValueError as e:
        print(e)