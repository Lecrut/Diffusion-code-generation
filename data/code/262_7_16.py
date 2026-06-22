class ListAnalyzer:

    def find_min_max(self, data):
        if not data or all((isinstance(item, list) for item in data)):
            return (None, None)
        minimum = float('inf')
        maximum = float('-inf')
        for item in data:
            if isinstance(item, list):
                sub_min, sub_max = self.find_min_max(item)
                if sub_min is not None and sub_min < minimum:
                    minimum = sub_min
                if sub_max is not None and sub_max > maximum:
                    maximum = sub_max
            else:
                if item < minimum:
                    minimum = item
                if item > maximum:
                    maximum = item
        return (minimum, maximum)
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_data = [[3, 1], [4, 1, 5], [9, 2]]
    result = analyzer.find_min_max(sample_data)
    print(result)