class ListMerger:
    def merge(self, list1, list2):
        return [*list1, *list2]

if __name__ == '__main__':
    merger = ListMerger()
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    merged_result = merger.merge(sample_list1, sample_list2)
    print(merged_result)