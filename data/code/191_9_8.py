class ListCombiner:
    def combine_lists(self, list_one, list_two):
        return list_one + list_two

if __name__ == '__main__':
    combiner = ListCombiner()
    result1 = combiner.combine_lists([1, 2, 3], [4, 5, 6])
    print(result1)
    result2 = combiner.combine_lists(['a', 'b'], ['c', 'd'])
    print(result2)