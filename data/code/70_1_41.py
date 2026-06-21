class ListChecker:
    def get_extremes(self, data):
        if not data:
            raise ValueError("Input sequence must not be empty")
        first = data[0]
        last = data[-1]
        return (first, last)

if __name__ == '__main__':
    checker = ListChecker()
    items = [5, 12, 8, 19, 3]
    extremes = checker.get_extremes(items)
    print(extremes)