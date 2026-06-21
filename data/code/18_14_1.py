def get_middle_value(numbers):
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty")
    if len(numbers) % 2 == 0:
        raise ValueError("The list must have an odd number of elements to have a single middle value")
    return numbers[len(numbers) // 2]

if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    result = get_middle_value(sample_array)
    print(result)