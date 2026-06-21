def find_largest(data):
    if not data:
        raise ValueError("Data cannot be empty")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_series = pd.Series([15, 8, 42, 3, 99, 22])
    try:
        largest_number = find_largest(sample_series)
        print(largest_number)
    except ValueError as e:
        print(e)