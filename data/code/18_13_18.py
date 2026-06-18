from operator import itemgetter

def is_first_greater_than_second(lst):
    """Check if the first element of a list is greater than the second."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3]
    result = is_first_greater_than_second(sample_list)
    print(f"{sample_list}[0] ({sample_list[0]}) > {sample_list}[1] ({sample_list[1]}): {result}")