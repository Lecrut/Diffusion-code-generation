class NumberDoubler:
    SAMPLE_VALUES = [10, 20, 30, 40, 50]

    @staticmethod
    def cycle_and_double(numbers):
        for number in numbers:
            print(number * 2)

if __name__ == '__main__':
    doubler = NumberDoubler()
    doubler.cycle_and_double(NumberDoubler.SAMPLE_VALUES)