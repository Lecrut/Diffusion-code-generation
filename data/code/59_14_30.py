class MiddleItemFinder:
    EMPTY_LIST_ERROR = 'The list is empty'

    @staticmethod
    def find_middle_item(lst):
        if not lst:
            raise ValueError(MiddleItemFinder.EMPTY_LIST_ERROR)
        n = len(lst)
        middle_index = n // 2
        if n % 2 == 0:
            return (lst[middle_index - 1] + lst[middle_index]) / 2
        else:
            return lst[middle_index]

if __name__ == '__main__':
    sample_list_odd = [3, 5, 7, 9, 11]
    sample_list_even = [4, 6, 8, 10, 12, 14]
    print(MiddleItemFinder.find_middle_item(sample_list_odd))
    print(MiddleItemFinder.find_middle_item(sample_list_even))