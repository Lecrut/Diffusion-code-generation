def rle_encode(data):
    if not data:
        return []
    result = []
    current_val = data[0]
    current_count = 1
    for val in data[1:]:
        if val == current_val:
            current_count += 1
        else:
            result.append([current_val, current_count])
            current_val = val
            current_count = 1
    result.append([current_val, current_count])
    return result

if __name__ == '__main__':
    input_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 4]
    output = rle_encode(input_data)
    print(output)