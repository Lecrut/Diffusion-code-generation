class ListChecker:
    def __init__(self):
        self._name = "ListExtremes"

    def get_extremes(self, data):
        if not hasattr(data, '__len__'):
            raise ValueError("Input must be a sequence")
        if len(data) == 0:
            raise ValueError("Sequence cannot be empty")
        first = data[0]
        last = data[-1]
        return (first, last)

if __name__ == '__main__':
    checker = ListChecker()
    numbers = [1, 2, 3, 4, 5]
    print(checker.get_extremes(numbers))
    words = ["alpha", "beta", "gamma"]
    print(checker.get_extremes(words))