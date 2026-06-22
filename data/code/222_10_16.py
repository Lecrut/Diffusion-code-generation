def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_list = [5, 7, 1, 8, 3, 4]
    result = find_minimum(sample_list)
    print(result)