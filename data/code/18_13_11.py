def check_first_greater_than_second(lst):
    """Returns True if lst[0] > lst[1], assuming len(lst) >= 2."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3, 8]
    result = check_first_greater_than_second(sample_list)
    print(f"{sample_list}[0] ({sample_list[0]}) is greater than {sample_list}[1] ({sample_list[1]}): {result}")

    # Additional test case where it's false
    sample_list_2 = [3, 5, 8]
    result_2 = check_first_greater_than_second(sample_list_2)
    print(f"{sample_list_2}[0] ({sample_list_2[0]}) is greater than {sample_list_2}[1] ({sample_list_2[1]}): {result_2}")