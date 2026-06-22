def rle_encode(text: str) -> str:
    if not text:
        return ""

    result = []
    count = 1
    current_char = text[0]

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = text[i]
            count = 1

    result.append(current_char + str(count))

    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded_output = rle_encode(sample_input)
    print(encoded_output)