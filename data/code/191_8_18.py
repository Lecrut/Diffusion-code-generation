class ListMerger:
    @staticmethod
    def merge_lists(list1, list2):
        return list1 + list2

if __name__ == '__main__':
    merger = ListMerger()
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    combined_list = merger.merge_lists(sample_list1, sample_list2)
    print(f"Merged List: {combined_list}")