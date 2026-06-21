class ListMerger:
    def merge(self, list1, list2):
        return [*list1, *list2]

if __name__ == '__main__':
    merger = ListMerger()
    result = merger.merge([1, 2, 3], ['a', 'b', 'c'])
    print(result)