def find_largest_integer(numbers):
    if not numbers:
        raise ValueError("The input list is empty.")
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

if __name__ == '__main__':
    sample_numbers = [100, 200, 50, 300, 75]
    print(find_largest_integer(sample_numbers))