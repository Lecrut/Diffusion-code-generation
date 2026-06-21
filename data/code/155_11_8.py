def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a list of integers")

def calculate_sum(data):
    return sum(data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    validate_input(sample_list)
    result = calculate_sum(sample_list)
    print(result)