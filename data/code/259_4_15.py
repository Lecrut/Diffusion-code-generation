def find_min_max(numbers):
    min_val = float('inf')
    max_val = float('-inf')
    for num in numbers:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [34, 12, 56, 78, 90, 23, 67]
    print(find_min_max(sample_values))