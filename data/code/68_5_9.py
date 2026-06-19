def absolute_differences(data):
    if not isinstance(data, list) or len(data) < 2:
        raise ValueError("Input must be a list with at least two elements.")
    
    for i in range(1, len(data)):
        yield abs(data[i] - data[i - 1])

if __name__ == '__main__':
    try:
        sample_list = [7, 3, 9, 2, 6]
        differences = absolute_differences(sample_list)
        result = list(differences)
        print(result)
    except ValueError as e:
        print(e)