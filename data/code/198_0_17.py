def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_data = [15, 3, 8, 22, 1]
    try:
        smallest = find_minimum(sample_data)
        print(smallest)
    except ValueError as e:
        print(e)