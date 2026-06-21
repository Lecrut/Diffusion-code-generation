def check_first_and_last(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    return lst[0], lst[-1]

if __name__ == '__main__':
    sample_list = [6, 7, 8, 9, 10]
    first, last = check_first_and_last(sample_list)
    print(first, last)