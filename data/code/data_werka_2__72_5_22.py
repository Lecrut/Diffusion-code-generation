class ListComparator:
    RESULT_GT = 'A > B'
    RESULT_LT = 'A < B'
    RESULT_EQ = 'A == B'

    @staticmethod
    def _compare_pair(a, b):
        if a > b:
            return ListComparator.RESULT_GT
        if a < b:
            return ListComparator.RESULT_LT
        return ListComparator.RESULT_EQ

    def compare(self, list_a, list_b):
        length = min(len(list_a), len(list_b))
        for i in range(length):
            yield ListComparator._compare_pair(list_a[i], list_b[i])

if __name__ == '__main__':
    a_list = [5, 10, 15]
    b_list = [3, 10, 12, 20]
    comparator = ListComparator()
    comparison_results = list(comparator.compare(a_list, b_list))
    print(comparison_results)