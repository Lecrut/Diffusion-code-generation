class ListAnalyzer:
    def __init__(self, data):
        self.data = data
    def get_minimum(self):
        if not self.data:
            raise ValueError("List cannot be empty")
        minimum = self.data[0]
        for element in self.data[1:]:
            if element < minimum:
                minimum = element
        return minimum
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9]
    analyzer = ListAnalyzer(sample_list)
    minimum_value = analyzer.get_minimum()
    print(minimum_value)