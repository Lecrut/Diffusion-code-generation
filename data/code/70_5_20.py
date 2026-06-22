class EdgeAnalyzer:
    def __init__(self, sequence):
        self.elements = sequence

    def fetch_extremities(self):
        count = len(self.elements)
        if count < 2:
            raise ValueError("Sequence must have at least two elements")
        return self.elements[0], self.elements[-1]

    def compute_span(self):
        first, last = self.fetch_extremities()
        if isinstance(first, (int, float)) and isinstance(last, (int, float)):
            return last - first
        return str(first) + str(last)

if __name__ == '__main__':
    analyzer = EdgeAnalyzer([100, 200, 300])
    print(analyzer.fetch_extremities())
    print(analyzer.compute_span())