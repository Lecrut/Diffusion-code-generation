def locate_minimum(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    minimum = values[0]
    for value in values[1:]:
        if value < minimum:
            minimum = value
    return minimum

if __name__ == '__main__':
    sample_data = [8.62, 3.45, 7.99, 1.23, 0.99]
    result = locate_minimum(sample_data)
    print(f"Smallest in {sample_data}: {result}")