class ListMerger:
    @staticmethod
    def merge(list1, list2):
        return list1 + list2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = ListMerger.merge(sample_list1, sample_list2)
    print(result)