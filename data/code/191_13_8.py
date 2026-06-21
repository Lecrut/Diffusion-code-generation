class ListMerger:
    def merge_lists(self, list1, list2):
        return list1 + list2

if __name__ == '__main__':
    merger = ListMerger()
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    combined = merger.merge_lists(list_a, list_b)
    print(combined)