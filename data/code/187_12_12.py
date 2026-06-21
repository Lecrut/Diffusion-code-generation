def find_greatest_item(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    greatest_item = numbers[0]
    for item in numbers:
        if item > greatest_item:
            greatest_item = item
    return greatest_item

if __name__ == '__main__':
    sample_values = [3.14, 1.618, 2.718, 0.577, 9.99]
    try:
        greatest_value = find_greatest_item(sample_values)
        print(greatest_value)
    except ValueError as e:
        print(e)