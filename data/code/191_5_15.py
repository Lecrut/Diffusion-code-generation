class ListCombiner:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def combine_using_or(self):
        return [x or y for x, y in zip_longest(self.list_a, self.list_b, fillvalue=False)]

if __name__ == '__main__':
    combiner = ListCombiner([True, False, True], [False, True])
    combined_result = combiner.combine_using_or()
    print(combined_result)