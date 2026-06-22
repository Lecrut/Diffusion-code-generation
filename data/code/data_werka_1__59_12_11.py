def is_valid_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        return False
    return True

def find_middle_item(numbers):
    if not is_valid_input(numbers):
        raise ValueError("Input must be a list of integers.")
    
    n = len(numbers)
    if n == 0:
        return None
    
    middle_index = n // 2
    if n % 2 == 1:
        return numbers[middle_index]
    else:
        return (numbers[middle_index - 1] + numbers[middle_index]) // 2

if __name__ == '__main__':
    sample_values = [3, 7, 2, 5, 8]
    try:
        result = find_middle_item(sample_values)
        print(result)
    except ValueError as e:
        print(e)