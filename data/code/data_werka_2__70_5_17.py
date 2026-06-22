class EndpointAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence

    def _validate_length(self):
        if len(self.sequence) < 2:
            raise ValueError("Sequence must have at least two elements")

    def get_endpoints(self):
        self._validate_length()
        start = self.sequence[0]
        end = self.sequence[-1]
        return start, end

if __name__ == '__main__':
    analyzer = EndpointAnalyzer([100, 200, 300, 400])
    endpoints = analyzer.get_endpoints()
    print(endpoints)