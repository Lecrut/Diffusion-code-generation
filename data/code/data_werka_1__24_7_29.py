class Utility:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    sample_values = [-10, 0, 10]
    for value in sample_values:
        print(f"{value} is negative: {Utility.is_negative(value)}")