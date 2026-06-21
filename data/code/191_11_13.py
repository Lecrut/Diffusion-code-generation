class ListMerger:
    @staticmethod
    def merge_lists(list_a, list_b):
        return [*list_a, *list_b]

if __name__ == '__main__':
    merger = ListMerger()
    result = merger.merge_lists([1, 2, 3], [4, 5, 6])
    print(result)