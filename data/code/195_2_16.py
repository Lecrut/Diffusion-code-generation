class ListComparator:
    @staticmethod
    def is_subset(subset, superset):
        return set(subset).issubset(set(superset))

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    list_c = [1, 2, 3, 5]
    list_d = [4, 3, 2, 1]

    print(f"list_a is subset of list_b: {ListComparator.is_subset(list_a, list_b)}")
    print(f"list_a is subset of list_c: {ListComparator.is_subset(list_a, list_c)}")
    print(f"list_b is subset of list_d: {ListComparator.is_subset(list_b, list_d)}")