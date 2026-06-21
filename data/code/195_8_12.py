class ListComparator:
    def compare_lists(self, list1, list2):
        return [(x, y) for x, y in zip(list1, list2) if x != y]

if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [1, 2, 2, 3]
    list_b = [3, 2, 1, 2]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    result1 = comparator.compare_lists(list_a, list_b)
    print(f"Differences (A vs B): {result1}")
    
    list_c = [1, 2, 3]
    list_d = [3, 1, 2]
    print(f"\nList C: {list_c}")
    print(f"List D: {list_d}")
    result2 = comparator.compare_lists(list_c, list_d)
    print(f"Differences (C vs D): {result2}")