class Utility:
    @staticmethod
    def is_positive(number):
        return number > 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.14, -2.71]
    for value in sample_values:
        result = Utility.is_positive(value)
        print(f"{value} is positive: {result}")