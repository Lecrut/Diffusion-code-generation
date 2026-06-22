def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_list = [42, 'hello', 3.14]
    result = get_first_element(sample_list)
    print(result)