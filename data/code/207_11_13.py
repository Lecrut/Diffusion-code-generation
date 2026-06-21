def find_maximum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    return max(data, key=lambda x: x)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_maximum(sample_list)
    print(result)