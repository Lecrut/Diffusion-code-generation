def all_elements_equal(lst):
    if not lst:
        return True
    first_element = lst[0]
    for element in lst[1:]:
        if element != first_element:
            return False
    return True

if __name__ == '__main__':
    sample_list = [8, 8, 8, 8]
    print(all_elements_equal(sample_list))