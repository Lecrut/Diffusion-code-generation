def find_largest_number(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    
    return largest

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(find_largest_number(sample_numbers))