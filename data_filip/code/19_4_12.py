def rle_encode(data):
    if not data:
        return []
    result = []
    current_value = data[0]
    count = 1
    for value in data[1:]:
        if value == current_value:
            count += 1
        else:
            result.append([count, current_value])
            current_value = value
            count = 1
    result.append([count, current_value])
    return result

if __name__ == '__main__':
    sample1 = [1, 1, 2, 2, 2, 3]
    sample2 = []
    sample3 = [5]
    sample4 = [1, 2, 3, 4, 5]
    print(rle_encode(sample1))
    print(rle_encode(sample2))
    print(rle_encode(sample3))
    print(rle_encode(sample4))