def get_first_and_last(lst):
    if not lst:
        raise ValueError("List must not be empty")
    first = lst[0]
    last = lst[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_first_and_last(sample_list)
    print(result)