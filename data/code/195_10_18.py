class ListComparator:
    @staticmethod
    def are_lists_identical(list1, list2):
        return set(list1) == set(list2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 3, 4, 5]
    list_c = [5, 4, 3, 2, 1]
    list_d = [1, 2, 3, 4, 6]
    list_e = [1, 2, 3, 4]

    print(f"Comparing {list_a} and {list_b}: {ListComparator.are_lists_identical(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {ListComparator.are_lists_identical(list_a, list_c)}")
    print(f"Comparing {list_a} and {list_d}: {ListComparator.are_lists_identical(list_a, list_d)}")
    print(f"Comparing {list_a} and {list_e}: {ListComparator.are_lists_identical(list_a, list_e)}")