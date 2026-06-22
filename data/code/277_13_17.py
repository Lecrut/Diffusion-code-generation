def count_elements(nested_list):
    if not isinstance(nested_list, list):
        raise ValueError("Input must be a list")
    
    count = 0
    for element in nested_list:
        if isinstance(element, list):
            count += count_elements(element)
        else:
            count += 1
    return count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    try:
        result = count_elements(sample_list)
        print(result)
    except ValueError as e:
        print(e)