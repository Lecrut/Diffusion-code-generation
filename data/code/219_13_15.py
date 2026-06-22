class MaxFinder:
    @staticmethod
    def find_largest_value(dictionary):
        if not dictionary:
            return None
        largest = float('-inf')
        for value in dictionary.values():
            if value > largest:
                largest = value
        return largest

if __name__ == '__main__':
    sample_dict = {'x': 10, 'y': 20, 'z': 5}
    analyzer = MaxFinder()
    print(analyzer.find_largest_value(sample_dict))