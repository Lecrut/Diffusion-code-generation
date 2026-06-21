def validate_input(*lists):
    for lst in lists:
        if not all((isinstance(item, (int, str)) for item in lst)):
            raise ValueError('All elements must be integers or strings.')

def find_common_elements(*lists):
    validate_input(*lists)
    set_objects = [set(lst) for lst in lists]
    common_elements = set.intersection(*set_objects)
    return sorted(list(common_elements))
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    result = find_common_elements(list_a, list_b)
    print(result)