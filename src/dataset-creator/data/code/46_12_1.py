import sys
def find_symmetric_difference(*lists):
    if len(lists) < 2:
        raise ValueError("At least two lists must be provided.")
    all_elements = set()
    for lst in lists:
        if isinstance(lst, (list, tuple)):
            all_elements.update(lst)
        else:
            raise TypeError(f"Expected list or tuple, got {type(lst).__name__}.")
    result_set = []
    for element in sorted(all_elements):
        count = sum(1 for lst in lists if element in lst)
        if count == 1:
            result_set.append(element)
    return result_set
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    list_c = [7, 8, 9]
    try:
        unique_elements = find_symmetric_difference(list_a, list_b)
        print(f"Symmetric difference between {list_a} and {list_b}:")
        print(unique_elements)
        all_unique = find_symmetric_difference(list_a, list_b, list_c)
        print("\nElements in exactly one of the three lists:")
        print(all_unique)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)