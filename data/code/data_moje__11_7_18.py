def get_last_element(lst):
    if not lst:
        return None
    return next(reversed(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)