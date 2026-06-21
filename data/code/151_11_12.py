class ListMerger:
    def merge_lists(self, list_a, list_b):
        list_a.extend(list_b)

if __name__ == '__main__':
    merger = ListMerger()
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merger.merge_lists(list1, list2)
    print("After combining (List A modified in place):")
    print("List A:", list1)