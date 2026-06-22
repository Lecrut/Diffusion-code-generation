def compress_string(input_string):
    if not input_string:
        return ""
    result = []
    current_char = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbccccdddd"
    compressed = compress_string(sample_string)
    print(compressed)
    empty_string = ""
    empty_result = compress_string(empty_string)
    print(empty_result)
    single_char = "z"
    single_result = compress_string(single_char)
    print(single_result)