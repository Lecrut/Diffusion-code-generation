class ListAnalyzer:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        if len(data) == 0:
            raise ValueError("List cannot be empty")
        self.data = data

    def get_middle_value(self):
        length = len(self.data)
        if length % 2 == 1:
            return self.data[length // 2]
        else:
            mid1 = self.data[length // 2 - 1]
            mid2 = self.data[length // 2]
            return (mid1 + mid2) / 2

if __name__ == '__main__':
    analyzer_odd = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer_odd.get_middle_value())

    analyzer_even = ListAnalyzer([1, 2, 3, 4])
    print(analyzer_even.get_middle_value())