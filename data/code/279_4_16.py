class NumberDoubler:
    @staticmethod
    def double_number(number):
        return number * 2

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    for value in sample_values:
        print(NumberDoubler.double_number(value))