MAX_VALUE = float('-inf')

def find_max_mixed(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_val = MAX_VALUE
    for item in numbers:
        if isinstance(item, (int, float)) and item > max_val:
            max_val = item
    return max_val

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, '10', -1]
    print(find_max_mixed(sample_values))