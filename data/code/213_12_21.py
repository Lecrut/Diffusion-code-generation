def validate_input(input_data):
    if not isinstance(input_data, set) or any(not isinstance(item, int) for item in input_data):
        raise ValueError("Input must be a set of integers")

def calculate_intersection(set1, set2):
    validate_input(set1)
    validate_input(set2)
    return set1.intersection(set2)

def calculate_union(set1, set2):
    validate_input(set1)
    validate_input(set2)
    return set1.union(set2)

def calculate_difference(set1, set2):
    validate_input(set1)
    validate_input(set2)
    return set1.difference(set2)

if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    intersection_result = calculate_intersection(set_a, set_b)
    union_result = calculate_union(set_a, set_b)
    difference_result = calculate_difference(set_a, set_b)

    print("Intersection:", intersection_result)
    print("Union:", union_result)
    print("Difference:", difference_result)