def calculate_total_sum(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")
    
    total = 0
    for number in numbers:
        total += number
    
    return total

if __name__ == '__main__':
    sample_list = [1, 5, 10, 2, 8]
    result = calculate_total_sum(sample_list)
    print(result)