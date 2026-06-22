class EndElementAnalyzer:
    MINIMUM_LENGTH = 2

    def __init__(self, sequence):
        self.sequence = sequence

    @staticmethod
    def _validate_length(length):
        if length < EndElementAnalyzer.MINIMUM_LENGTH:
            raise ValueError("Sequence must have at least two elements")

    def get_boundary_elements(self):
        self._validate_length(len(self.sequence))
        first = self.sequence[0]
        last = self.sequence[-1]
        return {"first": first, "last": last}

if __name__ == '__main__':
    analyzer = EndElementAnalyzer([100, 200, 300, 400])
    boundaries = analyzer.get_boundary_elements()
    print(boundaries)