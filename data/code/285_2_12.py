class ElementPairComparer:
    def __init__(self):
        self.comparison_results = {}

    @staticmethod
    def compare_pairs(pair1, pair2):
        return abs(pair1 - pair2) > 0.001

    def process_tuple(self, data):
        n = len(data)
        for i in range(n - 1):
            pair_key = (data[i], data[i + 1])
            self.comparison_results[pair_key] = self.compare_pairs(pair1=data[i], pair2=data[i + 1])

    def get_comparison_results(self):
        return self.comparison_results

if __name__ == '__main__':
    comparer = ElementPairComparer()
    sample_data = (1.0, 1.0005, 2.0, 2.001, 3.0, 3.0001)
    comparer.process_tuple(sample_data)
    print(comparer.get_comparison_results())