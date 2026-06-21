class ListChecker:
    def __init__(self, sequence):
        self._elements = sequence

    def _validate_sequence(self):
        if not hasattr(self._elements, '__len__'):
            raise TypeError("Input must be a sequence")
        if len(self._elements) == 0:
            raise ValueError("Sequence must contain at least one element")
        return True

    def get_first_and_last(self):
        self._validate_sequence()
        first = self._elements[0]
        last = self._elements[-1]
        return (first, last)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    checker = ListChecker(sample_list)
    output = checker.get_first_and_last()
    print(output)