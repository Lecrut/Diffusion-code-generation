def count_elements(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")
    
    element_count = {}
    for number in numbers:
        if number in element_count:
            element_count[number] += 1
        else:
            element_count[number] = 1
    
    return sorted(element_count.items())

if __name__ == '__main__':
    sample_values = [1, 2, 3, 2, 4, 3, 5]
    print(count_elements(sample_values))