import sys
def find_maximum(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30]
    result = find_maximum(input_data)
    print(result)