def find_smallest_number(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for num in data[1:]:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_numbers = [2.718, 3.14, -1.618, 9.99, 0.5]
    result = find_smallest_number(sample_numbers)
    print(result)