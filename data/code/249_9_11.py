def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_lists = [
        [1, 5, 2, 8, 3],
        [-10, -5, -20, -1],
        [42],
        [3.14, 2.71, 1.618],
        [100]
    ]
    for lst in sample_lists:
        print(f"List: {lst}, Largest: {find_largest(lst)}")