import sys
def find_max_value(numbers):
    if not numbers:
        return None
    max_val = -sys.maxsize
    for num in numbers:
        if isinstance(num, (int, float)):
            if num > max_val:
                max_val = num
    return max_val
if __name__ == '__main__':
    sample_list = [34, 78, 12, -50, 99]
    result = find_max_value(sample_list)
    if result is None:
        print("Error: Input list cannot be empty.")
    else:
        print(f"Maximum value in the list: {result}")