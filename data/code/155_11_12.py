sample_list = [10, 20, 30, 40, 50]

def validate_data(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements in the list must be integers")
    return data

def calculate_sum(data):
    return sum(validate_data(data))

if __name__ == '__main__':
    result = calculate_sum(sample_list)
    print(result)