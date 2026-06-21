class OddNumberCollector:
    def __init__(self):
        self.odd_numbers = []

    def collect(self, numbers):
        for number in numbers:
            if number % 2 != 0:
                self.odd_numbers.append(number)

    def get_odd_numbers(self):
        return self.odd_numbers

if __name__ == '__main__':
    collector = OddNumberCollector()
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    collector.collect(sample_data)
    print(collector.get_odd_numbers())