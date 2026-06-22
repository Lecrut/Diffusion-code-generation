class ListComparator:
    COMPARISON_THRESHOLD = 2

    @staticmethod
    def is_first_greater(lst):
        return lst[0] > lst[1] if len(lst) >= ListComparator.COMPARISON_THRESHOLD else False

if __name__ == '__main__':
    sample_list = [7, 4]
    result = ListComparator.is_first_greater(sample_list)
    print(result)