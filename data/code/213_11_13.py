def count_elements(numbers):
    if not numbers:
        return []
    
    element_count = {}
    for number in numbers:
        if number in element_count:
            element_count[number] += 1
        else:
            element_count[number] = 1
    
    result = sorted(element_count.items())
    return result

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 2, 3, 3, 4]
    print(count_elements(sample_numbers))