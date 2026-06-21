def encode_rle(input_string):
    if not input_string:
        return ""
    result = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append(f"{count}{input_string[i - 1]}")
            count = 1
    result.append(f"{count}{input_string[-1]}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbcdddd"
    encoded_result = encode_rle(sample_text)
    print(encoded_result)