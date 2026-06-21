class ListMerger:
    @staticmethod
    def merge_lists(list1, list2):
        return list1 + list2

if __name__ == '__main__':
    merger = ListMerger()
    result = merger.merge_lists([1, 2, 3], [4, 5, 6])
    print(result)