def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [3, 15, 2, 88, 1, 42, 9]
    maximum_value = find_maximum(sample_list)
    print(maximum_value)