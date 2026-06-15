class AverageCalculator:
    def get_averages(self, list_of_sets):
        averages = {}
        for s in list_of_sets:
            if s:
                average = sum(s) / len(s)
                averages[frozenset(s)] = average
            else:
                averages[frozenset(s)] = 0.0
        return averages
if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data = [
        {1, 2, 3},
        {4, 5, 6, 7},
        {8, 9}
    ]
    results = calculator.get_averages(sample_data)
    print(results)