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
    sample_input = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
    compressed = compress_rle(sample_input)
    print(compressed)
    sample_input2 = [5, 5, 5, 5]
    compressed2 = compress_rle(sample_input2)
    print(compressed2)
    sample_input3 = [1, 2, 3, 4, 5]
    compressed3 = compress_rle(sample_input3)
    print(compressed3)
    sample_input4 = []
    compressed4 = compress_rle(sample_input4)
    print(compressed4)