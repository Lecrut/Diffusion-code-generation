class NumberAggregator:
    def __init__(self):
        self.total = 0

    def add_number(self, number):
        self.total += number

    def get_total(self):
        return self.total

if __name__ == '__main__':
    aggregator = NumberAggregator()
    numbers = [10, 25, 40, 5]
    for number in numbers:
        aggregator.add_number(number)
    print(aggregator.get_total())