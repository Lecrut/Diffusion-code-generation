def find_minimum(numbers):
    if not numbers:
        raise ValueError("Empty list provided")
    
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    
    return min_value

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 12]
    try:
        print(find_minimum(sample_list))
    except ValueError as e:
        print(e)