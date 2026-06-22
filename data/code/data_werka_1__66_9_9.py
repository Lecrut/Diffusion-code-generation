class ArrayAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_adjacent_greater_pairs(self):
        indices = []
        for i in range(len(self.data) - 1):
            if self.data[i + 1] > self.data[i]:
                indices.append(i)
        return indices

if __name__ == '__main__':
    sample_array = [10, 20, 15, 30, 25, 40]
    analyzer = ArrayAnalyzer(sample_array)
    result = analyzer.find_adjacent_greater_pairs()
    print(result)

    another_sample = [5, 3, 8, 6, 7, 2, 9]
    another_analyzer = ArrayAnalyzer(another_sample)
    another_result = another_analyzer.find_adjacent_greater_pairs()
    print(another_result)