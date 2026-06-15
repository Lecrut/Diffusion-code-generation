def find_min_manual(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    sample_list = [45, 12, 88, 3, 56, 21]
    result = find_min_manual(sample_list)
    print(result)