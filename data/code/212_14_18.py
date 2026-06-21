def min_max_pairwise(numbers):
    if not numbers:
        return None, None
    
    min_val = max_val = numbers[0]
    
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [34, 78, 12, 56, 90, 23, 67]
    print(min_max_pairwise(sample_values))