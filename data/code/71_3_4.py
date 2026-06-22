class ListAnalyzer:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        if len(data) == 0:
            raise ValueError("List cannot be empty")
        self.data = data

    def get_middle_value(self):
        length = len(self.data)
        if length % 2 == 0:
            mid_index = length // 2
            return (self.data[mid_index - 1] + self.data[mid_index]) / 2
        else:
            mid_index = length // 2
            return self.data[mid_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer.get_middle_value())
    
    analyzer2 = ListAnalyzer([1, 2, 3, 4])
    print(analyzer2.get_middle_value())