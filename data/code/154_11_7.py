class FrequencyCalculator:
    def __init__(self):
        self.frequency = {}

    def add_item(self, item):
        if item in self.frequency:
            self.frequency[item] += 1
        else:
            self.frequency[item] = 1

    def get_frequency(self):
        return self.frequency

if __name__ == '__main__':
    calculator = FrequencyCalculator()
    sample_list = [1, 2, 3, 4, 5, 2, 3, 1]
    for item in sample_list:
        calculator.add_item(item)
    print(f"Frequency of items: {calculator.get_frequency()}")