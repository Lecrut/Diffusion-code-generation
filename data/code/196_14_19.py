class ListCombiner:
    def combine_lists(self, list1, list2):
        return list1 + list2

if __name__ == '__main__':
    combiner = ListCombiner()
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    result = combiner.combine_lists(sample_list_a, sample_list_b)
    print(result)