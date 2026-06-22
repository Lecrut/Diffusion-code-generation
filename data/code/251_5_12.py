def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for number in data[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [9, 24, 35, 7, 88, 12]
    result = find_largest(sample_list)
    print(result)