def validate_input(data):
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the list must be numeric")

def aggregate_values(data):
    validate_input(data)
    return sum(data)

if __name__ == '__main__':
    sample_list = [10, 25, 30, 5]
    total = aggregate_values(sample_list)
    print(total)