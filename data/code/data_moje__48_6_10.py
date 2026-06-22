import operator

def find_max_value(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    current_max = numbers[0]
    for num in numbers:
        if operator.gt(num, current_max):
            current_max = num
    return current_max

if __name__ == '__main__':
    sample_values = [12, 45, 7, 89, 34, 99, 2, 56]
    result = find_max_value(sample_values)
    print(result)