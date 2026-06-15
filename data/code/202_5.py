def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest
if __name__ == '__main__':
    sample_list = [12, 45, 67, 89, 34, 91, 5]
    result = find_largest(sample_list)
    print(result)