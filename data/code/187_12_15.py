def find_max_element(floats):
    if not floats:
        raise ValueError('Input list cannot be empty')
    max_element = floats[0]
    for floating_point in floats:
        if floating_point > max_element:
            max_element = floating_point
    return max_element
if __name__ == '__main__':
    sample_values = [2.718, 3.14159, 0.618, 1.414, 0.577]
    try:
        result = find_max_element(sample_values)
        print(result)
    except ValueError as e:
        print(e)