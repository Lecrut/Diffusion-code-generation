class Utility:

    @staticmethod
    def is_positive(number):
        return number > 0

if __name__ == '__main__':
    sample_values = [-10, -1, 0, 1, 10]
    for value in sample_values:
        print(f"{value} is positive: {Utility.is_positive(value)}")