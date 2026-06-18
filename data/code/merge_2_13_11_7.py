def find_max(numbers):
    if not numbers:
        return None
    max_val = float('-inf')
    for num in numbers:
        if num > max_val:
            max_val = num
    return int(max_val)
if __name__ == '__main__':
    sample_data = [3, 71, -45, 2.89, 0]
    result = find_max(sample_data)
    print(result)