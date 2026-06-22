def find_min_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    data = [3.14, 2.71, 1.618, 0.577, 1.414]
    min_value = find_min_value(data)
    print(min_value)