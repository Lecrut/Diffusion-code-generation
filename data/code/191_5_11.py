class ListCombiner:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b
        self.length = max(len(list_a), len(list_b))

    def combine(self):
        return [a or b for a, b in zip_longest(self.list_a, self.list_b, fillvalue=False)]

if __name__ == '__main__':
    combiner = ListCombiner([True, False], [False, True])
    result = combiner.combine()
    print(result)