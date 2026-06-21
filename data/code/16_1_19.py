def compress_rle(input_list):
    if not input_list:
        return []

    compressed = []
    current_value = input_list[0]
    count = 1

    for i in range(1, len(input_list)):
        if input_list[i] == current_value:
            count += 1
        else:
            if count == 1:
                compressed.append(current_value)
            else:
                compressed.append((current_value, count))
            current_value = input_list[i]
            count = 1

    if count == 1:
        compressed.append(current_value)
    else:
        compressed.append((current_value, count))

    return compressed

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 7, 7, 7, 8]
    result = compress_rle(sample_list)
    print(result)