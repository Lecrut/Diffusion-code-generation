def get_last_element(lst):
    if not lst:
        raise IndexError('Cannot get last element of an empty list')
    return lst[-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)