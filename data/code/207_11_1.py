def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    current_max = data[0]
    for i in range(1, len(data)):
        if data[i] > current_max:
            current_max = data[i]
    return current_max
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_maximum(sample_list)
    print(result)