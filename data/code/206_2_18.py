def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    minimum = float('inf')
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, -2.1, 0.0]
    try:
        print(find_minimum(sample_values))
    except ValueError as e:
        print(e)