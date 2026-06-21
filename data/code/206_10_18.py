def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_minimum(sample_list)
    print(result)