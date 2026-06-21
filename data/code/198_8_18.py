def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2]
    print(find_smallest(sample_list))