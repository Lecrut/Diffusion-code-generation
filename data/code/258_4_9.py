class PairAverager:
    @staticmethod
    def calculate_average(pair):
        return (pair[0] + pair[1]) / 2

    @classmethod
    def average_pairs(cls, pair_dict):
        if not isinstance(pair_dict, dict) or not all(isinstance(k, tuple) and len(k) == 2 for k in pair_dict.keys()):
            raise ValueError("Input must be a dictionary with tuple keys of length 2")
        averages = {}
        for pair, value in pair_dict.items():
            avg = cls.calculate_average(pair)
            averages[pair] = avg
        return averages

if __name__ == '__main__':
    sample_data = {(1, 2): 3, (4, 5): 9, (6, 7): 13}
    result = PairAverager.average_pairs(sample_data)
    print(result)