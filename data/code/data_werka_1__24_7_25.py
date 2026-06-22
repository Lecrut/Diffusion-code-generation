class Utility:
    @staticmethod
    def is_negative(number):
        return number < 0

if __name__ == '__main__':
    sample_values = [-10, -1, 0, 1, 10]
    results = {value: Utility.is_negative(value) for value in sample_values}
    print(results)