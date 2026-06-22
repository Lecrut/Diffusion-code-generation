def compress_rle(input_string):
    if not input_string:
        return ""
    result = []
    current_char = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = input_string[i]
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAABBB"
    print(compress_rle(sample_data))
    print(compress_rle("A"))
    print(compress_rle("ABBBBCCCCCCCCAA"))
    print(compress_rle(""))