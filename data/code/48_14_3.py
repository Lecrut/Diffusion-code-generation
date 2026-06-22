def find_max_element(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    data = [3.14, 2.71, 1.618, 9.81, 0.577]
    result = find_max_element(data)
    print(result)