def is_valid_input(numbers):
    return isinstance(numbers, list) and all(isinstance(x, (int, float)) for x in numbers)

def find_middle_item(numbers):
    if not is_valid_input(numbers):
        raise ValueError("Input must be a list of integers or floats.")
    
    n = len(numbers)
    if n == 0:
        return None
    
    middle_index = n // 2
    if n % 2 == 1:
        return numbers[middle_index]
    else:
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2

if __name__ == '__main__':
    sample_input = [3, 7, 2, 9, 5]
    try:
        middle_item = find_middle_item(sample_input)
        print(middle_item)
    except ValueError as e:
        print(e)