def calculate_sum(data):
    if not all(isinstance(item, int) for item in data):
        raise ValueError("All elements in the list must be integers.")
    return sum(data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = calculate_sum(sample_list)
    print(result)