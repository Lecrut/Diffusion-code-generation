class ListChecker:
    def get_extremes(self, data):
        if not hasattr(data, '__getitem__') or len(data) == 0:
            raise ValueError("Input must be a non-empty sequence")
        first = data[0]
        last = data[-1]
        return (first, last)

if __name__ == '__main__':
    checker = ListChecker()
    numbers = [1, 2, 3, 4, 5]
    words = ['alpha', 'beta', 'gamma']
    print(checker.get_extremes(numbers))
    print(checker.get_extremes(words))