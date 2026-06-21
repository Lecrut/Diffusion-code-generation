def find_maximum(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10.5, 4.3, 25.7, 8.9, 30.2]
    maximum_value = find_maximum(sample_list)
    print(maximum_value)