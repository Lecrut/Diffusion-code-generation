class EdgeAnalyzer:
    def __init__(self, sequence):
        self._elements = sequence

    def verify_boundary(self):
        if len(self._elements) < 2:
            raise ValueError("Sequence must have at least two elements")
        return self._elements[0], self._elements[-1]

    def get_span(self):
        if len(self._elements) < 2:
            return None
        first = self._elements[0]
        last = self._elements[-1]
        return last - first

    def describe_edges(self):
        if len(self._elements) < 2:
            return "Empty or single item"
        return f"Start: {self._elements[0]}, End: {self._elements[-1]}"

if __name__ == '__main__':
    analyzer = EdgeAnalyzer([100, 200, 300, 400])
    bounds = analyzer.verify_boundary()
    print(bounds)
    print(analyzer.get_span())
    print(analyzer.describe_edges())