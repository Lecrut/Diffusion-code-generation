def run_length_encode(text: str) -> str:
    if not text:
        return text

    result = []
    current_char = text[0]
    count = 1
    length = len(text)

    for i in range(1, length):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1

    if count > 1:
        result.append(str(count))
    result.append(current_char)

    compressed = "".join(result)
    
    if len(compressed) >= length:
        return text
    return compressed

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    encoded1 = run_length_encode(sample1)
    print(encoded1)

    sample2 = "abc"
    encoded2 = run_length_encode(sample2)
    print(encoded2)

    sample3 = ""
    encoded3 = run_length_encode(sample3)
    print(encoded3)

    sample4 = "aabbcc"
    encoded4 = run_length_encode(sample4)
    print(encoded4)