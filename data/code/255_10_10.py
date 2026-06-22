MAX_NUMBER = float('-inf')

def find_max_value(numbers):
    if not numbers:
        return None
    max_val = MAX_NUMBER
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 30, 1]
    print(find_max_value(sample_numbers))