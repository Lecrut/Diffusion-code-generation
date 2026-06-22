class ListChecker:
    def __init__(self):
        self.min_length = 1

    def _validate_sequence(self, data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        if len(data) < self.min_length:
            raise ValueError("Sequence must contain at least one element")
        return True

    def get_extremes(self, data):
        self._validate_sequence(data)
        return (data[0], data[-1])

if __name__ == '__main__':
    checker = ListChecker()
    sample_data = [5, 12, 8, 19, 3]
    result = checker.get_extremes(sample_data)
    print(result)