def validate_input(data):
    if not hasattr(data, '__iter__'):
        raise TypeError("Input must be an iterable")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError("All items in the iterable must be numbers")

def compute_mean(data):
    validate_input(data)
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(compute_mean(sample_data))