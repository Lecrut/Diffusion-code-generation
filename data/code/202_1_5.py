def find_largest(numbers):
    if not numbers:
        raise ValueError("The input tuple is empty")
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = (3.14, 2.71, 1.618)
    print(find_largest(sample_values))