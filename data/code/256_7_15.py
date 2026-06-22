def find_range(data):
    try:
        return max(data) - min(data)
    except ValueError:
        return None

if __name__ == '__main__':
    sample_data = [3.14159, 1.0, 9.81, 2.71828, 0.5, 100.0, -5.5, 3.14159]
    range_result = find_range(sample_data)
    print(range_result)