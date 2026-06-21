class ListMerger:
    @staticmethod
    def merge(list1, list2):
        return list1 + list2

if __name__ == '__main__':
    merger = ListMerger()
    result = merger.merge([1, 2, 3], [4, 5, 6])
    print(result)