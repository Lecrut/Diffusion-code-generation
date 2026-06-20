class Averager:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return 0
        try:
            return sum(self.numbers) / len(self.numbers)
        except TypeError:
            raise ValueError("Input contains non-numeric values.")

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    averager = Averager(sample_numbers)
    print(averager.calculate_average())