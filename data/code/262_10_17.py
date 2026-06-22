def find_min_max(numbers):
    if not numbers:
        return None, None
    min_num = max_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num

if __name__ == '__main__':
    sample_values = [45, 23, 89, 67, 10, 34]
    result = find_min_max(sample_values)
    print(f"Min: {result[0]}, Max: {result[1]}")