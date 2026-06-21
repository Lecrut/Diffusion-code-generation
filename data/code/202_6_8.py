def find_largest(data):
    if not data:
        return None
    largest = max(data)
    return largest

if __name__ == '__main__':
    sample_series = [15, 8, 42, 3, 99, 22]
    print(find_largest(sample_series))