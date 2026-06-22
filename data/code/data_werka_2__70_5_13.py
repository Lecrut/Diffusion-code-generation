class EndpointsAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence

    def _validate_length(self):
        length = len(self.sequence)
        if length < 2:
            raise ValueError("Sequence must have at least two elements")
        return length

    def get_endpoints(self):
        self._validate_length()
        return self.sequence[0], self.sequence[-1]

if __name__ == '__main__':
    analyzer = EndpointsAnalyzer([100, 200, 300, 400])
    print(analyzer.get_endpoints())