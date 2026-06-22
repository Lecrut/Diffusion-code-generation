def count_nested_elements(nested_list):
    total_count = 0
    stack = [nested_list]
    while stack:
        current_element = stack.pop()
        if isinstance(current_element, list):
            stack.extend(reversed(current_element))
        else:
            total_count += 1
    return total_count
if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
    result = count_nested_elements(sample_list)
    print(result)