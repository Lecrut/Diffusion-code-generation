def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_list = [34.5, 12.3, 56.7, 9.8, 88.9, 23.4, 7.6]
    result = find_minimum(sample_list)
    print(result)