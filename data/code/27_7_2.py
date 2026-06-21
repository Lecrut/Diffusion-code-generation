def rle_encode(data):
    if not data:
        return ""
    result = []
    index = 0
    while index < len(data):
        count = 1
        while index + 1 < len(data) and data[index] == data[index + 1]:
            index += 1
            count += 1
        result.append(str(count) + data[index])
        index += 1
    return "".join(result)

if __name__ == "__main__":
    input_string = "AABBCC"
    encoded_result = rle_encode(input_string)
    print(encoded_result)