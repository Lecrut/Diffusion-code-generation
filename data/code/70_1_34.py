class ListChecker:
    MIN_LENGTH = 1

    def get_extremes(self, data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input must be a sequence")
        if len(data) < self.MIN_LENGTH:
            raise ValueError("Sequence must contain at least one element")
        return (data[0], data[-1])

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    checker = ListChecker()
    print(checker.get_extremes(sample_data))