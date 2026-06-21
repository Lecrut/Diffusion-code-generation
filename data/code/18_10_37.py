class ListComparator:

    @staticmethod
    def is_first_greater_than_second(lst):
        return lst[0] > lst[1]
if __name__ == '__main__':
    sample_list_1 = [10, 5]
    sample_list_2 = [3, 7]
    sample_list_3 = [4.5, 4.5]
    print(ListComparator.is_first_greater_than_second(sample_list_1))
    print(ListComparator.is_first_greater_than_second(sample_list_2))
    print(ListComparator.is_first_greater_than_second(sample_list_3))