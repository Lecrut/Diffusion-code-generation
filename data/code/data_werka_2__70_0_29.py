def check_first_and_last(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    return lst[0], lst[-1]

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    try:
        first, last = check_first_and_last(sample_list)
        print(first, last)
    except (TypeError, ValueError) as e:
        print(e)