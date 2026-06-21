class ListComparer:
    def __init__(self, list_a, list_b):
        self.set_a = set(list_a)
        self.set_b = set(list_b)

    def find_common_elements(self):
        return self.set_a.intersection(self.set_b)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    comparer = ListComparer(sample_list1, sample_list2)
    common_elements = comparer.find_common_elements()
    print(common_elements)