class NumberCycler:
    def __init__(self, numbers):
        self.numbers = numbers

    def cycle_and_square(self):
        for number in self.numbers:
            print(number ** 2)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    cycler = NumberCycler(sample_values)
    cycler.cycle_and_square()