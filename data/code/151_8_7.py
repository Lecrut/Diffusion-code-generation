class ListMerger:
    @staticmethod
    def merge_and_sort_lists(list1, list2):
        combined_set = set(list1 + list2)
        return sorted(combined_set)

if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 4.8]
    sample_list2 = [2.9, 1.2, 6.0]
    result = ListMerger.merge_and_sort_lists(sample_list1, sample_list2)
    print(result)