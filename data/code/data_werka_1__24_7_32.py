class Utility:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    test_values = [10, -5, 0, -3.5]
    results = {value: Utility.is_negative(value) for value in test_values}
    print(results)