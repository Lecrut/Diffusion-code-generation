def find_min_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    
    min_val = numbers[0]
    for number in numbers[1:]:
        if number < min_val:
            min_val = number
    return min_val

if __name__ == '__main__':
    sample_numbers = [34, 78, 12, 56, 90]
    print(find_min_element(sample_numbers))