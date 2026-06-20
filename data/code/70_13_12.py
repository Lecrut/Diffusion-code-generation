def print_first_last(lst):
    if not lst:
        return None
    first = lst[0]
    last = lst[-1] if len(lst) > 1 else first
    return first, last

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(print_first_last(sample_list))