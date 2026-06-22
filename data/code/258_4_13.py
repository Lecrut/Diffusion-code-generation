class PairAverages:
    def __init__(self, data):
        self.data = data

    def calculate_averages(self):
        averages = {}
        for pair in self.data.keys():
            avg = (pair[0] + pair[1]) / 2
            averages[pair] = avg
        return averages

if __name__ == '__main__':
    sample_data = {(1, 2): 3, (4, 5): 9, (6, 7): 13}
    calculator = PairAverages(sample_data)
    result = calculator.calculate_averages()
    print(result)