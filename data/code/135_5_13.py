def validate_list_comprehensions(comp1, comp2):
    if not isinstance(comp1, list) or not isinstance(comp2, list):
        raise ValueError("Both inputs must be lists.")
    return True

def compare_list_comprehensions(list_comp1, list_comp2):
    validate_list_comprehensions(list_comp1, list_comp2)
    return set(list_comp1) == set(list_comp2)

if __name__ == '__main__':
    sample_comp1 = [x**2 for x in range(5)]
    sample_comp2 = [x*x for x in range(5)]
    result = compare_list_comprehensions(sample_comp1, sample_comp2)
    print(result)