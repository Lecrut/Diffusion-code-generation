def check_first_and_last(lst):
    if not lst:
        return None, None
    return lst[0], lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    first, last = check_first_and_last(sample_list)
    print(first, last)