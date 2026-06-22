class PairAverageCalculator:
    @staticmethod
    def calculate_average(pair):
        return (pair[0] + pair[1]) / 2

    @classmethod
    def average_pairs(cls, pair_dict):
        averages = {}
        for pair in pair_dict.keys():
            avg = cls.calculate_average(pair)
            averages[pair] = avg
        return averages

if __name__ == '__main__':
    sample_data = {(1, 2): 3, (4, 5): 9, (6, 7): 13}
    calculator = PairAverageCalculator()
    result = calculator.average_pairs(sample_data)
    print(result)