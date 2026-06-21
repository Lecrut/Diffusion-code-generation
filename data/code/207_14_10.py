def find_maximum(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    maximum = find_maximum(sample_list)
    print(maximum)