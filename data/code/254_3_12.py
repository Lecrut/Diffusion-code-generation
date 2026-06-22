def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum

if __name__ == '__main__':
    sample_data = [5, 2, 8, 1, 9, -10, 0, 5, -3, 42]
    print(f"Minimum of {sample_data}: {find_minimum(sample_data)}")