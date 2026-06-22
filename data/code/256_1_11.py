def find_min(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def calculate_range(numbers):
    if not numbers:
        return 0
    min_val = find_min(numbers)
    max_val = find_max(numbers)
    return max_val - min_val

if __name__ == '__main__':
    sample_list = [10, 5, 20, 3, 15]
    result = calculate_range(sample_list)
    print(result)