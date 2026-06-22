def calculate_sum(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    result = calculate_sum(sample_list)
    print(f"The sum of {sample_list} is: {result}")