class ListAnalyzer:
    def analyze_list(self, input_list):
        return [(item, input_list.count(item)) for item in set(input_list)]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = analyzer.analyze_list(sample_list)
    print(result)