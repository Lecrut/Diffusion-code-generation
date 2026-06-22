class DictAnalyzer:
    @staticmethod
    def find_largest_value(dictionary):
        if not dictionary:
            return None
        return max(dictionary.values(), default=None)

if __name__ == '__main__':
    sample_dict = {'x': 10, 'y': 20, 'z': 5}
    analyzer = DictAnalyzer()
    print(analyzer.find_largest_value(sample_dict))