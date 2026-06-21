def rle_encode(input_string):
    if not input_string:
        return ""
    result = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append(input_string[i - 1] + str(count))
            count = 1
    result.append(input_string[-1] + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AABBCC"
    encoded_value = rle_encode(sample_input)
    print(encoded_value)