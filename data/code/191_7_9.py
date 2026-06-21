class ListMerger:
    @staticmethod
    def merge_lists(list_x, list_y):
        return list_x + list_y

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = ['a', 'b', 'c']
    merged_result = ListMerger.merge_lists(sample_list_a, sample_list_b)
    print(merged_result)