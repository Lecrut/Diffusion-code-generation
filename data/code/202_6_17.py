class SeriesAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_largest(self):
        if not self.data:
            return None
        largest = self.data[0]
        for item in self.data[1:]:
            if item > largest:
                largest = item
        return largest

if __name__ == '__main__':
    sample_series = SeriesAnalyzer([15, 8, 42, 3, 99, 22])
    print(sample_series.find_largest())