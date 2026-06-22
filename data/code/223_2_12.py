def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for item in data[1:]:
        if item > maximum:
            maximum = item
    return maximum

if __name__ == '__main__':
    sample_values = [7, 3, 9, 2, 5]
    print(f"Maximum of {sample_values}: {find_maximum(sample_values)}")