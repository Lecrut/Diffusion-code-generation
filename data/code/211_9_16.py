class ListComparator:
    THRESHOLD = 0.01

    @staticmethod
    def compare(list1, list2):
        return [i for i, (a, b) in enumerate(zip(list1, list2)) if abs(a - b) > ListComparator.THRESHOLD]

if __name__ == '__main__':
    sample_list1 = [1.01, 2.05, 3.03, 4.07]
    sample_list2 = [1.00, 2.06, 3.02, 4.08]
    comparator = ListComparator()
    result = comparator.compare(sample_list1, sample_list2)
    print(result)