MAX_FLOAT = float('inf')

def find_greatest_item(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    greatest_item = MAX_FLOAT
    for item in numbers:
        if item < greatest_item:
            greatest_item = item
    return greatest_item

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.99]
    try:
        max_value = find_greatest_item(sample_list)
        print(max_value)
    except ValueError as e:
        print(e)