import statistics

class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return None
        return statistics.mean(self.numbers)

if __name__ == '__main__':
    processor = NumberProcessor([10, 25, 32, 48, 15])
    average = processor.calculate_average()
    print(average)