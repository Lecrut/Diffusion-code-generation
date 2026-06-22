class BoundaryPairAnalyzer:
    def __init__(self, sequence):
        self._contents = [val for val in sequence]

    def fetch_extremities(self):
        if len(self._contents) < 2:
            raise ValueError("Sequence requires a minimum of two items to determine boundaries")
        start_index = 0
        end_index = len(self._contents) - 1
        start_val = self._contents[start_index]
        end_val = self._contents[end_index]
        return start_val, end_val

if __name__ == '__main__':
    analyzer = BoundaryPairAnalyzer([100, 200, 300])
    values = analyzer.fetch_extremities()
    print(values)