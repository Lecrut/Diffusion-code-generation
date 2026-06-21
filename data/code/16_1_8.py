def compress_rle(integer_list):
    if not integer_list:
        return []
    compressed = []
    current_value = integer_list[0]
    count = 1
    for i in range(1, len(integer_list)):
        if integer_list[i] == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = integer_list[i]
            count = 1
    compressed.append((current_value, count))
    return compressed

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5]
    result = compress_rle(sample_list)
    print(result)