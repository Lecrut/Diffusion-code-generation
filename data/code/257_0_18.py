def find_extremes(numbers):
    if not numbers or len(numbers) < 2:
        raise ValueError("List must contain at least two integers")
    
    return max(numbers), min(numbers)

def calculate_difference(numbers):
    max_val, min_val = find_extremes(numbers)
    return abs(max_val - min_val)

if __name__ == '__main__':
    sample_numbers = [10, 3, 5, 8, 2]
    result = calculate_difference(sample_numbers)
    print(result)