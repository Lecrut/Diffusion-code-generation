def calculate_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum
if __name__ == '__main__':
    sample_list = [10, 3.5, 20, -5.2, 15]
    result = calculate_range(sample_list)
    print(result)