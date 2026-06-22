def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]
    return largest

if __name__ == '__main__':
    sample_list = [34, 2, 98, 56, 76, 12]
    result = find_largest(sample_list)
    print(result)