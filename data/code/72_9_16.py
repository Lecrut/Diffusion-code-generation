def is_valid_index(index, lst):
    return index >= 0 and index < len(lst)

def compare_elements_at_indices(lists, indices):
    results = {}
    for i in indices:
        if not is_valid_index(i, lists[0]):
            raise IndexError(f"Index {i} out of bounds for list of length {len(lists[0])}")
        values = [lst[i] if is_valid_index(i, lst) else None for lst in lists]
        results[i] = compare_elements(values)
    return results

def compare_elements(values):
    if len(set(values)) == 1:
        return f"equal: {values[0]}"
    min_val = min([val for val in values if val is not None])
    max_val = max([val for val in values if val is not None])
    if min_val < max_val:
        return f"less than: {min_val}"
    elif min_val > max_val:
        return f"greater than: {max_val}"
    else:
        return "equal"

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [11, 21, 31, 41]
    list3 = [12, 22, 32, 42]
    indices = [0, 1, 2, 3, 4]
    print(compare_elements_at_indices([list1, list2, list3], indices))