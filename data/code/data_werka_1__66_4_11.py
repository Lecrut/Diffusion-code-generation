def is_strictly_increasing_pairwise(numbers):
    def validate_input(data):
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("All elements must be integers or floats.")
        if len(data) < 2:
            return False

    def generate_booleans(data):
        return [data[i] < data[i + 1] for i in range(len(data) - 1)]

    if not validate_input(numbers):
        return []

    return generate_booleans(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 4.2, 5.0, 6.1, 7.8]
    result = is_strictly_increasing_pairwise(sample_values)
    print(result)