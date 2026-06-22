def calculate_total(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements must be numbers")
    
    return sum(numbers)

if __name__ == '__main__':
    numbers = [10, 25, 40, 5]
    total_sum = calculate_total(numbers)
    print(total_sum)