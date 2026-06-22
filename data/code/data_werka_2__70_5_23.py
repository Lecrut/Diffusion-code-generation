class EndValidator:
    MINIMUM_LENGTH = 2

    def __init__(self, sequence):
        self._elements = list(sequence)

    def get_boundary_pair(self):
        if len(self._elements) < self.MINIMUM_LENGTH:
            raise ValueError("Sequence must have at least two items")
        return (self._elements[0], self._elements[-1])

if __name__ == '__main__':
    validator = EndValidator([100, 200, 300])
    print(validator.get_boundary_pair())