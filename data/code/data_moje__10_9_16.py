def get_first_element(lst):
    if not lst:
        raise IndexError("List is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [42, 17, 99, 3]
    result = get_first_element(sample_list)
    print(result)