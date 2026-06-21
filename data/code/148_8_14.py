def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 8, 7]
    result = find_largest(sample_list)
    print(result)
    sample_list_2 = [100, 50, 200, 10]
    result_2 = find_largest(sample_list_2)
    print(result_2)