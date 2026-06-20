class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    processor1 = NumberProcessor((1, 2, 3, 4, 5))
    print(f"Average of {processor1.numbers}: {processor1.calculate_average()}")

    processor2 = NumberProcessor(())
    print(f"Average of {processor2.numbers}: {processor2.calculate_average()}")

    processor3 = NumberProcessor((10, 20, 30))
    print(f"Average of {processor3.numbers}: {processor3.calculate_average()}")

    processor4 = NumberProcessor((-1, 5, 10))
    print(f"Average of {processor4.numbers}: {processor4.calculate_average()}")