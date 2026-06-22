def get_head(lst):
    if not lst:
        raise IndexError('Cannot retrieve head from an empty list')
    return lst[0]
if __name__ == '__main__':
    sample_list = [42, 'hello', 3.14, True, None]
    result = get_head(sample_list)
    print(result)