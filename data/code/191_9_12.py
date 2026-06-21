class ListCombiner:
    @staticmethod
    def combine_lists(list_one, list_two):
        combined_set = set(list_one)
        combined_set.update(list_two)
        return list(combined_set)

if __name__ == '__main__':
    combiner = ListCombiner()
    result = combiner.combine_lists([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    print(result)
    result2 = combiner.combine_lists(['apple', 'banana', 'cherry'], ['banana', 'date', 'elderberry'])
    print(result2)