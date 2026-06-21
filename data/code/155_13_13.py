def calculate_sum(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    return sum(numbers)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    total = calculate_sum(data)
    print("Total sum:", total)