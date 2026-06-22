class ListComparator:
    @staticmethod
    def is_first_greater_than_second(lst):
        return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list_1 = [15, 10]
    sample_list_2 = [2, 3]
    sample_list_3 = [7.8, 7.8]
    
    print(f"Is the first element of {sample_list_1} greater than the second? {ListComparator.is_first_greater_than_second(sample_list_1)}")
    print(f"Is the first element of {sample_list_2} greater than the second? {ListComparator.is_first_greater_than_second(sample_list_2)}")
    print(f"Is the first element of {sample_list_3} greater than the second? {ListComparator.is_first_greater_than_second(sample_list_3)}")