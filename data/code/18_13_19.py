def check_first_greater_than_second(lst):
    """Returns True if the first element of lst is greater than the second, assuming len(lst) >= 2."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3, 8, 1]
    result = check_first_greater_than_second(sample_list)
    print(f"Is {sample_list[0]} greater than {sample_list[1]}? {result}")

    # Additional test case where it is not true
    sample_list_2 = [2, 4, 6, 9]
    result_2 = check_first_greater_than_second(sample_list_2)
    print(f"Is {sample_list_2[0]} greater than {sample_list_2[1]}? {result_2}")