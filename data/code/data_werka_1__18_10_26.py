class ListEvaluator:
    @staticmethod
    def is_first_greater_than_second(lst):
        return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list1 = [15, 10]
    sample_list2 = [3, 7]
    sample_list3 = [8.5, 8.5]
    
    result1 = ListEvaluator.is_first_greater_than_second(sample_list1)
    result2 = ListEvaluator.is_first_greater_than_second(sample_list2)
    result3 = ListEvaluator.is_first_greater_than_second(sample_list3)
    
    print(f"Is the first element of {sample_list1} greater than the second? {result1}")
    print(f"Is the first element of {sample_list2} greater than the second? {result2}")
    print(f"Is the first element of {sample_list3} greater than the second? {result3}")