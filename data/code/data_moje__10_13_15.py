def get_head(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list.')
    if not lst:
        raise ValueError('List is empty.')
    return lst[0]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    head_value = get_head(sample_list)
    print(head_value)