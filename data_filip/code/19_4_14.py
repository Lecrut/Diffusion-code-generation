def rle_encode(data):
    if not data:
        return []
    result = []
    current_value = data[0]
    count = 1
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
    sample = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]
    print(rle_encode(sample))
    print(rle_encode([]))
    print(rle_encode([42]))