def first_greater_than_second(lst):
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list_1 = [8, 4]
    sample_list_2 = [3, 7]
    sample_list_3 = [-1, -2]
    
    result1 = first_greater_than_second(sample_list_1)
    result2 = first_greater_than_second(sample_list_2)
    result3 = first_greater_than_second(sample_list_3)
    
    print(f"Is the first element greater than the second in {sample_list_1}? {result1}")
    print(f"Is the first element greater than the second in {sample_list_2}? {result2}")
    print(f"Is the first element greater than the second in {sample_list_3}? {result3}")