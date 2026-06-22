def are_elements_equal(elements):
    if not elements:
        return True
    first_element = elements[0]
    for element in elements:
        if element != first_element:
            return False
    return True

if __name__ == '__main__':
    sample_list = [5, 5, 5, 5]
    print(are_elements_equal(sample_list))