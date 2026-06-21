class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_mean(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    stats = Statistics([3.5, 2.1, 4.8, 5.0])
    print(stats.calculate_mean())