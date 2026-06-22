class NumberDoubler:
    SAMPLE_VALUES = [10, 20, 30, 40, 50]

    @staticmethod
    def double_numbers(numbers):
        for number in numbers:
            print(number * 2)

if __name__ == '__main__':
    NumberDoubler.double_numbers(NumberDoubler.SAMPLE_VALUES)