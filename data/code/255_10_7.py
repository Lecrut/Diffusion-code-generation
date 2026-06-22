def find_maximum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 30, 1]
    try:
        result = find_maximum(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)