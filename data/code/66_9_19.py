class ArrayAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_adjacent_greater_indices(self):
        indices = []
        for i in range(len(self.data) - 1):
            if self.data[i + 1] > self.data[i]:
                indices.append(i)
        return indices

if __name__ == '__main__':
    sample_array = [3, 5, 2, 8, 6, 7, 4]
    analyzer = ArrayAnalyzer(sample_array)
    result = analyzer.find_adjacent_greater_indices()
    print(result)