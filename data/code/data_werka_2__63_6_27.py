def get_first_element(lst):
    if not lst:
        raise ValueError("The list is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [42, 17, 9, 3]
    print(get_first_element(sample_list))