def validate_data(data):
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the list must be numeric")

def aggregate_numeric_values(data):
    validate_data(data)
    return sum(data)

if __name__ == '__main__':
    sample_list = [10, 25, 30, 5]
    total = aggregate_numeric_values(sample_list)
    print(total)