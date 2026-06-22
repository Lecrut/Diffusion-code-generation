def find_min_max(nested_list):
    if not all(isinstance(item, (list, int)) for item in nested_list):
        raise ValueError("Input must be a list of integers or lists")

    min_val = float('inf')
    max_val = float('-inf')

    def traverse(sub_list):
        nonlocal min_val, max_val
        for element in sub_list:
            if isinstance(element, list):
                traverse(element)
            else:
                if element < min_val:
                    min_val = element
                if element > max_val:
                    max_val = element

    traverse(nested_list)

    return min_val, max_val

if __name__ == '__main__':
    sample_data = [10, [5, 20], 3, [15, [25]]]
    print(find_min_max(sample_data))