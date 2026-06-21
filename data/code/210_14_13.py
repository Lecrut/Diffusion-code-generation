class DataAnalyzer:
    def __init__(self, data=None):
        self.data = data if data is not None else []

    def set_data(self, data):
        self.data = data

    def get_span(self):
        if not self.data:
            return 0
        minimum = min(self.data)
        maximum = max(self.data)
        return maximum - minimum

if __name__ == '__main__':
    analyzer1 = DataAnalyzer([10, 5, 20, 3, 15])
    print(f"Span of {analyzer1.data}: {analyzer1.get_span()}")

    analyzer2 = DataAnalyzer([5.5, 1.2, 8.9, 3.0])
    print(f"\nSpan of {analyzer2.data}: {analyzer2.get_span()}")

    analyzer3 = DataAnalyzer([])
    print(f"\nSpan of empty data: {analyzer3.get_span()}")