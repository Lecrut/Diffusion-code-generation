def compress_rle(input_list):
    if not input_list:
        return []
    result = []
    current_value = input_list[0]
    count = 1
    for i in range(1, len(input_list)):
        if input_list[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = input_list[i]
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
    compressed = compress_rle(sample_list)
    print(compressed)