def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_data = [5, 2, 8, 1]
    print(find_smallest(sample_data))