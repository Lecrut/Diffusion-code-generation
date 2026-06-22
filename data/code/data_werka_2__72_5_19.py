def compare_lists(list_a, list_b):
    COMPARE_GT = 'A > B'
    COMPARE_LT = 'A < B'
    COMPARE_EQ = 'A == B'
    limit = min(len(list_a), len(list_b))
    index = 0
    while index < limit:
        val_a = list_a[index]
        val_b = list_b[index]
        if val_a > val_b:
            result = COMPARE_GT
        elif val_a < val_b:
            result = COMPARE_LT
        else:
            result = COMPARE_EQ
        yield result
        index += 1

class ListComparator:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def get_comparisons(self):
        return compare_lists(self.list_a, self.list_b)

if __name__ == '__main__':
    data_first = [10, 20, 30, 40]
    data_second = [10, 15, 35, 45, 50]
    comparator = ListComparator(data_first, data_second)
    comparisons = list(comparator.get_comparisons())
    print(comparisons)