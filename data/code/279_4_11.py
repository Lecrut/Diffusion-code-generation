class NumberDoubler:
    def __init__(self, numbers):
        self.numbers = numbers

    def double_and_print(self):
        for number in self.numbers:
            print(number * 2)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    doubler = NumberDoubler(sample_values)
    doubler.double_and_print()