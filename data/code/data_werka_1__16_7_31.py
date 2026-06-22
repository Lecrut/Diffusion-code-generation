class Utility:

    @staticmethod
    def is_positive(number):
        return number > 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.5]
    results = {value: Utility.is_positive(value) for value in sample_values}
    print(results)