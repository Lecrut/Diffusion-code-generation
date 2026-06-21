class FrequencyAnalyzer:
    def __init__(self, input_list):
        self.input_list = input_list

    def get_frequencies(self):
        return [(item, self.input_list.count(item)) for item in set(self.input_list)]

if __name__ == '__main__':
    analyzer = FrequencyAnalyzer([1, 2, 3, 4, 5])
    print(analyzer.get_frequencies())