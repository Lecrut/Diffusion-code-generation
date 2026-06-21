def find_largest(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
    print(find_largest(sample_data))