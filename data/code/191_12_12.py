import itertools

class ListMerger:
    @staticmethod
    def merge_lists(list1, list2):
        return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    merger = ListMerger()
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    combined_list = merger.merge_lists(sample_list1, sample_list2)
    print(combined_list)