def calculate_sum(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numbers")
    return sum(numbers)

if __name__ == '__main__':
    data = [10, 25, 30, 45, 50]
    print(calculate_sum(data))