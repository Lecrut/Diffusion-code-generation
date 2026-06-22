class Utility:
    @staticmethod
    def is_positive(number):
        return number > 0

if __name__ == '__main__':
    test_values = [42, -3.14, 0, 7, -8]
    for value in test_values:
        result = Utility.is_positive(value)
        print(f"Is {value} positive? {result}")