class ListMerger:
    @staticmethod
    def merge(list_x, list_y):
        return list_x + list_y

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    merged_result = ListMerger.merge(sample_list1, sample_list2)
    print(merged_result)