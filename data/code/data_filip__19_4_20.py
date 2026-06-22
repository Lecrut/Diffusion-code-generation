def run_length_encode(data):
    if not data:
        return []
    result = []
    count = 1
    current_value = data[0]
    for item in data[1:]:
        if item == current_value:
            count += 1
        else:
            result.append([count, current_value])
            current_value = item
            count = 1
    result.append([count, current_value])
    return result

if __name__ == '__main__':
    sample1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
    sample2 = []
    sample3 = [7]
    sample4 = [1, 2, 3, 4, 5]
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))