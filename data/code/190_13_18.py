def validate_input(target, lst):
    if not isinstance(lst, list):
        raise ValueError("The second argument must be a list.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numbers.")

def is_element_in_list(target, lst):
    validate_input(target, lst)
    return target in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(is_element_in_list(target_value, sample_list))