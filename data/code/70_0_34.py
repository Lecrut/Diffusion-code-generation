def check_first_and_last(lst):
    if not lst:
        raise ValueError("The list cannot be empty")
    return lst[0], lst[-1]

if __name__ == '__main__':
    sample_list = [2, 4, 6, 8, 10]
    first, last = check_first_and_last(sample_list)
    print(first, last)