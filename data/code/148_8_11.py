def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_list = [23, 45, 67, 89, 10, 32, 54]
    result = find_largest(sample_list)
    print(result)

    sample_list_2 = [-5, -1, -8, -3, -12, -7]
    result_2 = find_largest(sample_list_2)
    print(result_2)