class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_span(self):
        if not self.data:
            return None
        minimum = min(self.data)
        maximum = max(self.data)
        return maximum - minimum

if __name__ == '__main__':
    analyzer_1 = DataAnalyzer([10, 5, 20, 15])
    span_1 = analyzer_1.calculate_span()
    print(f"Data: [10, 5, 20, 15], Span: {span_1}")

    analyzer_2 = DataAnalyzer([3.14, 1.618, 2.718])
    span_2 = analyzer_2.calculate_span()
    print(f"Data: [3.14, 1.618, 2.718], Span: {span_2}")

    analyzer_3 = DataAnalyzer([5])
    span_3 = analyzer_3.calculate_span()
    print(f"Data: [5], Span: {span_3}")

    analyzer_4 = DataAnalyzer([])
    span_4 = analyzer_4.calculate_span()
    print(f"Data: [], Span: {span_4}")