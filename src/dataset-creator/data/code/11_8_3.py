def verify_nested_equality(nested_list):
    if not nested_list:
        return True
    first_element = nested_list[0]
    for element in nested_list[1:]:
        try:
            set_first = {first_element}
            set_current = {element}
            if not (set_first == set_current):
                return False
        except TypeError:
            if first_element != element:
                return False
    return True
if __name__ == '__main__':
    sample_data = [1, 2, 3]
    result = verify_nested_equality(sample_data)
    print(result)