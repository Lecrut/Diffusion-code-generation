def find_difference(numbers):
    if not numbers:
        raise ValueError("The tuple must contain at least one number.")
    max_num = float('-inf')
    min_num = float('inf')
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num - min_num

if __name__ == '__main__':
    sample_values = (7.8, 3.4, 9.1, 2.5, 6.0)
    print(find_difference(sample_values))