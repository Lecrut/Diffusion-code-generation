def get_first_element(lst):
    first_element = None
    if lst:
        first_element = lst[0]
    return first_element

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    result = get_first_element(sample_list)
    print(result)