import itertools

class ListCombiner:
    @staticmethod
    def combine_lists(list1, list2):
        return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    combiner = ListCombiner()
    combined_list = combiner.combine_lists(sample_list1, sample_list2)
    print(combined_list)