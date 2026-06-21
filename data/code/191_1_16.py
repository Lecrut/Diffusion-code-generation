class ListCombiner:
    @staticmethod
    def combine_lists(list_a, list_b):
        return list(set(list_a + list_b))

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 2]
    list_b = [4, 5, 6, 7, 1]
    result = ListCombiner.combine_lists(list_a, list_b)
    print(result)