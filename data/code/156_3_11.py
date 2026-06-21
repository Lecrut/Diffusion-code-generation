def compute_average(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list of floats")
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data = [2.1, 3.9, 5.7, 6.3]
    average_result = compute_average(sample_data)
    print(average_result)