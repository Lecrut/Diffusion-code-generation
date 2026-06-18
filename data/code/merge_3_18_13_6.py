def check_first_greater_than_second(lst):
    """Returns True if lst[0] > lst[1], assuming len(lst) >= 2."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3, 8]
    result = check_first_greater_than_second(sample_list)
    print(f"Is {sample_list}[0] greater than {sample_list}[1]? {result}")