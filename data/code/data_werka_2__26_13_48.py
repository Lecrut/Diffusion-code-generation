class IntegerComparison:

    def __init__(self):
        self.results = []

    def compare(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('Both arguments must be integers.')
        result = a > b
        self.results.append(result)
        return result
if __name__ == '__main__':
    comparator = IntegerComparison()
    print(comparator.compare(10, 5))
    print(comparator.compare(3, 8))
    print(comparator.compare(7, 7))
    print(comparator.results)