def rle_encode(data):
    if not data:
        return []
    result = []
    current_value = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            result.append([count, current_value])
            current_value = data[i]
            count = 1
    result.append([count, current_value])
    return result

if __name__ == '__main__':
    sample_input = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5]
    print(rle_encode(sample_input))
    empty_input = []
    print(rle_encode(empty_input))