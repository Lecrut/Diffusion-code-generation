def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 21]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)