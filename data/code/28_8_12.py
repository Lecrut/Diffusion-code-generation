def compress_rle(int_list):
    if not int_list:
        return []

    result = []
    current_value = int_list[0]
    count = 1

    for i in range(1, len(int_list)):
        if int_list[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = int_list[i]
            count = 1

    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
    compressed = compress_rle(sample_data)
    print(compressed)