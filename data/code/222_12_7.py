def find_min_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    data = [3.5, 2.1, 4.8, 1.9, 5.6, 0.7]
    min_value = find_min_value(data)
    print(min_value)