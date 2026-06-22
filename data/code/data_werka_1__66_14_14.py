class ArrayAnalyzer:

    def __init__(self, data):
        self.data = data

    def compare_adjacent(self):
        return [self.data[i] > self.data[i - 1] for i in range(1, len(self.data))]
if __name__ == '__main__':
    sample_array = [3.0, 5.5, 2.1, 8.9, 6.7]
    analyzer = ArrayAnalyzer(sample_array)
    result = analyzer.compare_adjacent()
    print(result)
    another_array = [1.0, 2.0, 3.0, 4.0, 5.0]
    another_analyzer = ArrayAnalyzer(another_array)
    another_result = another_analyzer.compare_adjacent()
    print(another_result)