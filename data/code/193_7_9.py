def calculate_sum(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")
    return sum(numbers)

if __name__ == '__main__':
    data = [10, 25, 30, 45, 50]
    result = calculate_sum(data)
    print(result)