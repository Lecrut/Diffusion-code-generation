import sys

def check_first_greater_than_second(lst):
    """Returns True if the first element is greater than the second, assuming list has at least 2 elements."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3, 8, 2]
    result = check_first_greater_than_second(sample_list)
    print(f"List: {sample_list}")
    print(f"First ({sample_list[0]}) > Second ({sample_list[1]}): {result}")