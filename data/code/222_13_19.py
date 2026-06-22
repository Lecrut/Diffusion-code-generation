def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_input = "10 5 -3 22 8"
    try:
        input_data = sample_input.split()
        numeric_list = [int(item) for item in input_data]
        minimum_value = find_minimum(numeric_list)
        print(minimum_value)
    except ValueError as e:
        print(e)