class ListComparer:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def find_common_elements_ordered(self):
        common_elements = []
        set_b = set(self.list_b)
        for item in self.list_a:
            if item in set_b and item not in common_elements:
                common_elements.append(item)
        return common_elements

if __name__ == '__main__':
    comparer1 = ListComparer([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    print(f"Common elements of {comparer1.list_a} and {comparer1.list_b}: {comparer1.find_common_elements_ordered()}")

    comparer2 = ListComparer([10, 20, 30, 40], [30, 40, 50, 60])
    print(f"Common elements of {comparer2.list_a} and {comparer2.list_b}: {comparer2.find_common_elements_ordered()}")

    comparer3 = ListComparer(['a', 'b', 'c', 'd'], ['c', 'd', 'e', 'f'])
    print(f"Common elements of {comparer3.list_a} and {comparer3.list_b}: {comparer3.find_common_elements_ordered()}")