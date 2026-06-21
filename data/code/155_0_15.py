def calculate_sum(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    return sum(numbers)

if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    result = calculate_sum(sample_list)
    print(result)