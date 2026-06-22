class NumberCycler:
    def __init__(self, numbers):
        self.numbers = numbers

    def cycle_and_double(self):
        for number in self.numbers:
            print(number * 2)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    cycler = NumberCycler(sample_values)
    cycler.cycle_and_double()