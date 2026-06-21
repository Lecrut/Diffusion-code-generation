def find_largest(numbers):
    if not numbers:
        return None
    
    max_value = numbers[0]
    
    for number in numbers:
        if number > max_value:
            max_value = number
            
    return max_value

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    largest = find_largest(sample_list)
    print(largest)