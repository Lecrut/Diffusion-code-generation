def find_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None

if __name__ == '__main__':
    sample_list = [42, 3.14, 'hello', True]
    first_element = find_first_element(sample_list)
    print(first_element)