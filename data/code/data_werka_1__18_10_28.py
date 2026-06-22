def is_first_greater_than_second(lst):
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list_1 = [20, 15]
    result_1 = is_first_greater_than_second(sample_list_1)
    print(f"Is the first element of {sample_list_1} greater than the second? {result_1}")

    sample_list_2 = [8, 8]
    result_2 = is_first_greater_than_second(sample_list_2)
    print(f"Is the first element of {sample_list_2} greater than the second? {result_2}")

    sample_list_3 = [-3, -7]
    result_3 = is_first_greater_than_second(sample_list_3)
    print(f"Is the first element of {sample_list_3} greater than the second? {result_3}")