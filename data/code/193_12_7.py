def aggregate_numeric_values(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("All elements in the list must be numeric")
    return sum(data)

if __name__ == '__main__':
    sample_list = [10, 25, 30, 5]
    result = aggregate_numeric_values(sample_list)
    print(result)