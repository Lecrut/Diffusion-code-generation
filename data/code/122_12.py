class NumberAverager:
    def __init__(self, numbers):
        self.numbers = numbers
    def compute_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    averager = NumberAverager(sample_list)
    average = averager.compute_average()
    print(average)