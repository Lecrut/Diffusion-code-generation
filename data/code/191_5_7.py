class ListCombiner:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def combine(self):
        return [x or y for x, y in zip(self.list_a, self.list_b)]

if __name__ == '__main__':
    combiner = ListCombiner([True, False, True], [False, True, False])
    combined_result = combiner.combine()
    print(combined_result)