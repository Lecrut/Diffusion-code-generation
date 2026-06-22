def find_middle_item(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements in the list must be integers or floats.")
    
    n = len(numbers)
    if n == 0:
        return None
    
    middle_index = n // 2
    if n % 2 == 1:
        return numbers[middle_index]
    else:
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2

if __name__ == '__main__':
    try:
        sample_input = [3, 6, 9, 12, 15]
        middle_item = find_middle_item(sample_input)
        print(middle_item)
    except ValueError as e:
        print(e)