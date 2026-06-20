class ListMerger:
    def merge_lists_at_index(self, list1, list2, index):
        return [(list1[index], list2[index])]

if __name__ == '__main__':
    merger = ListMerger()
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    sample_index = 1
    result = merger.merge_lists_at_index(sample_list1, sample_list2, sample_index)
    print(result)