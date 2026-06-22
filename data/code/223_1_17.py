def find_largest_element(elements):
    max_value = elements[0]
    for element in elements:
        if element > max_value:
            max_value = element
    return max_value

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, 1.414]
    largest_element = find_largest_element(sample_values)
    print(largest_element)