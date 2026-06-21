class ListComparator:
    @staticmethod
    def are_identical(list1, list2):
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

if __name__ == '__main__':
    list_a = [1, 5, 3, 7, 9]
    list_b = [1, 5, 4, 7, 9]
    result = ListComparator.are_identical(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print("Lists are identical:" if result else "Lists are different")