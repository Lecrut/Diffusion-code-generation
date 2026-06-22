def get_last_element(lst):
    if not lst:
        raise IndexError("list index out of range")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)