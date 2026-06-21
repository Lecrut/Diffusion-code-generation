def validate_lists(*lists):
    if not all(isinstance(lst, list) for lst in lists):
        raise ValueError("All arguments must be lists")
    if any(len(lst) == 0 for lst in lists):
        raise ValueError("No empty lists allowed")

def find_common_elements(*lists):
    validate_lists(*lists)
    return sorted(set.intersection(*map(set, lists)))

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    list_c = [5, 9, 10, 4]
    result = find_common_elements(list_a, list_b, list_c)
    print(result)