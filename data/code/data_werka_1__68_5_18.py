def absolute_differences(data):
    if not isinstance(data, list) or len(data) < 2:
        raise ValueError("Input must be a list with at least two elements.")
    
    for i in range(len(data) - 1):
        yield abs(data[i+1] - data[i])

if __name__ == '__main__':
    sample_list = [7, 3, 9, 1, 5]
    try:
        differences = list(absolute_differences(sample_list))
        print(differences)
    except ValueError as e:
        print(e)