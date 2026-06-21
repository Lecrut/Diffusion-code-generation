class ListMerger:
    def merge(self, list_x, list_y):
        return list_x + list_y

if __name__ == '__main__':
    merger = ListMerger()
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    result = merger.merge(sample_list1, sample_list2)
    print(result)