import itertools

class ListMerger:
    @staticmethod
    def merge(list1, list2):
        return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    merger = ListMerger()
    sample_list1 = [1, 5, 2, 8, 5]
    sample_list2 = [8, 3, 1, 9, 2]
    result = merger.merge(sample_list1, sample_list2)
    print(result)