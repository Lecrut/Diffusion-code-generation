def find_max(numbers):
    if not numbers or len(numbers) == 0:
        raise ValueError("Input list must contain at least one numeric value.")
    maximum = float('-inf')
    for num in numbers:
        current_num = int(num) if isinstance(num, float) else num
        if current_num > maximum:
            maximum = current_num
    return maximum
if __name__ == '__main__':
    sample_data = [10.5, 23, -42, 78.9, 5]
    result = find_max(sample_data)
    print(result)