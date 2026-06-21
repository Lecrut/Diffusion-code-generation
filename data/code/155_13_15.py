def validate_data(data):
    if not isinstance(data, list) or not all(isinstance(item, int) for item in data):
        raise ValueError("Data must be a list of integers")

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    validate_data(data)
    total = sum(data)
    print(total)