class ListComparator:
    @staticmethod
    def compare_lists(list1, list2):
        return all(a <= b for a, b in zip(list1, list2))

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]
    result = ListComparator.compare_lists(list_a, list_b)
    print(result)