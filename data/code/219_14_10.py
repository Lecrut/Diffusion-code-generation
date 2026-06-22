def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return max(numbers)

if __name__ == '__main__':
    input_data = [15, 8, 42, 3, 99, 27, 50]
    result = find_largest(input_data)
    print(result)