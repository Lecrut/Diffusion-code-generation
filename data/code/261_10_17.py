def validate_input(data):
    if not isinstance(data, list) or len(data) != 5:
        raise ValueError("Input must be a list of exactly five integers")

def calculate_median(data):
    validate_input(data)
    sorted_data = sorted(data)
    return sorted_data[2]

if __name__ == '__main__':
    sample_values = [10, 5, 8, 12, 3]
    print(calculate_median(sample_values))