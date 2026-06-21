def find_maximum(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10.5, 4.2, 25.8, 8.9, 30.1]
    maximum = find_maximum(sample_list)
    print(maximum)