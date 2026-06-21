class ListMerger:
    def merge_lists(self, list1, list2):
        return list1 + list2

if __name__ == '__main__':
    merger = ListMerger()
    first_input = [1, 2, 3]
    second_input = [4, 5, 6]
    merged_result = merger.merge_lists(first_input, second_input)
    print(merged_result)