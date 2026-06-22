def validate_input(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    for item in lst:
        if not (isinstance(item, int) or isinstance(item, str)):
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
    validate_input(sample_list)
    print(are_elements_unique(sample_list))