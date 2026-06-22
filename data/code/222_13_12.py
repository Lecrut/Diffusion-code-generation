def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    input_data = ["10", "5", "-3", "22", "8"]
    try:
        numbers = [int(x) for x in input_data]
        minimum_value = find_minimum(numbers)
        print(minimum_value)
    except ValueError as e:
        print(e)