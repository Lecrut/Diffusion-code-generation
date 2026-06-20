class ListMerger:
    @staticmethod
    def merge_lists_at_index(list1, list2, index):
        if len(list1) > index and len(list2) > index:
            return [(list1[index], list2[index])]
        else:
            raise IndexError("Index out of bounds for one of the lists")

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    sample_index = 1
    try:
        merged_result = ListMerger.merge_lists_at_index(sample_list1, sample_list2, sample_index)
        print(merged_result)
    except IndexError as e:
        print(e)