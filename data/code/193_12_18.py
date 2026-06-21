def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError("All items in the list must be numbers")

def aggregate_values(data):
    validate_input(data)
    return sum(data)

if __name__ == '__main__':
    sample_list = [10, 25, 30, 5]
    total = aggregate_values(sample_list)
    print(total)