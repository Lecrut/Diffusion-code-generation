def validate_input(lst):
    if not all(isinstance(item, (int, str)) for item in lst):
        raise ValueError("List contains non-hashable elements")

def are_elements_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        validate_input(sample_list)
        print(are_elements_unique(sample_list))
    except ValueError as e:
        print(f"Error: {e}")

    sample_list_with_non_hashable = [1, 2, 'a', {'b': 2}, 5]
    try:
        validate_input(sample_list_with_non_hashable)
        print(are_elements_unique(sample_list_with_non_hashable))
    except ValueError as e:
        print(f"Error: {e}")