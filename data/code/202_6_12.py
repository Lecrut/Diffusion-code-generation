def find_largest(data):
    if not data:
        return None
    return max(data)

if __name__ == '__main__':
    sample_series = [15, 8, 42, 3, 99, 22]
    largest_number = find_largest(sample_series)
    print(largest_number)