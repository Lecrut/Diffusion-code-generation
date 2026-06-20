class ListComparator:

    @staticmethod
    def are_lists_equal(list1, list2):
        return len(list1) == len(list2) and set(list1).intersection(set(list2)) == set(list1)
if __name__ == '__main__':
    list_a = [3, 1, 4, 1, 5, 9]
    list_b = [9, 5, 1, 4, 1, 3]
    result = ListComparator.are_lists_equal(list_a, list_b)
    print(result)