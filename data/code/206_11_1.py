def find_minimum(data):
    if not data:
        return None
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    input_list = [45, 12, 89, 3, 67, 22]
    result = find_minimum(input_list)
    print(result)
    empty_list = []
    result_empty = find_minimum(empty_list)
    print(result_empty)