def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        current = numbers[i]
        if current > max_val:
            max_val = current
    return max_val
if __name__ == '__main__':
    sample_data = [3.5, 7.2, -4.8, 9.1, 0.0, 12.3]
    result = find_max(sample_data)
    print(result)