def find_largest_value(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    
    return largest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2, 9, 4]
    print(find_largest_value(sample_values))