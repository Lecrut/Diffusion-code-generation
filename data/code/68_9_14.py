class DifferenceCalculator:
    @staticmethod
    def find_difference(num1, num2):
        return abs(num1 - num2)

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3.5, 7.8),
        (-4, -9),
        (0, 0),
        (100, 200)
    ]

    for value1, value2 in sample_values:
        result = DifferenceCalculator.find_difference(value1, value2)
        print(f"The absolute difference between {value1} and {value2} is {result}")