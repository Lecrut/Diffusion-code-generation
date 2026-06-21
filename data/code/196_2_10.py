class ListMerger:
    @staticmethod
    def merge_lists(list1, list2):
        return list1 + list2

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    result = ListMerger.merge_lists(sample_list_a, sample_list_b)
    print(result)