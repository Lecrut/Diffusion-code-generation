def rle_encode(data):
    if not data:
        return ""
    result_parts = []
    current_char = data[0]
    count = 1
    for char, next_char in zip(data, data[1:] + chr(0)):
        if char == next_char:
            count += 1
        else:
            if count > 1:
                result_parts.append(str(count))
            result_parts.append(char)
            count = 1
    return "".join(result_parts)

if __name__ == '__main__':
    sample_input = 'AAAAABBBS'
    output_value = rle_encode(sample_input)
    print(output_value)