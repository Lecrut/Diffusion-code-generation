def find_min_item(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    data = [3.14, 2.71, 1.618, 0.577, 4.669]
    print(find_min_item(data))