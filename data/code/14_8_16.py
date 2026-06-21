class SequenceAccessor:
    def __init__(self, sequence):
        self._sequence = sequence

    def get_third(self):
        if len(self._sequence) < 3:
            raise IndexError("Sequence too short")
        return self._sequence[2]

if __name__ == '__main__':
    test_data = [100, 200, 355, 400, 500]
    accessor = SequenceAccessor(test_data)
    print(accessor.get_third())