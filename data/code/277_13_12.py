def count_elements(nested_list):
    total_count = 0
    stack = nested_list[:]
    
    while stack:
        element = stack.pop()
        if isinstance(element, list):
            stack.extend(element)
        else:
            total_count += 1
    
    return total_count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    result = count_elements(sample_list)
    print(result)