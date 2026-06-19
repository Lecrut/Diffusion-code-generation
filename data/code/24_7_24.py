class Utility:
    @staticmethod
    def is_negative(number):
        return number < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.14, 27]
    results = {value: Utility.is_negative(value) for value in sample_values}
    print(results)