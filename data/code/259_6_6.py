def parse_numbers(numbers_str):
    try:
        return [int(num) for num in numbers_str.split(',')]
    except ValueError as e:
        raise ValueError("Invalid input: All elements must be integers.") from e

def find_extremes(numbers_list):
    if not numbers_list or len(numbers_list) == 0:
        raise ValueError("Input list is empty.")
    
    smallest = min(numbers_list)
    largest = max(numbers_list)
    return smallest, largest

if __name__ == '__main__':
    sample_values = "3,1,4,1,5,9,2,6,5,3,5"
    numbers = parse_numbers(sample_values)
    result = find_extremes(numbers)
    print(result)