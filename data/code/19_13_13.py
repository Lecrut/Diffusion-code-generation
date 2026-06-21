def rle_encode(data):
    if not data:
        return ""
    result = []
    count = 1
    prev_char = data[0]
    for i in range(1, len(data)):
        char = data[i]
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            prev_char = char
            count = 1
    result.append(f"{count}{prev_char}")
    return "".join(result)

if __name__ == "__main__":
    sample_text = "aaabbbcccaa"
    encoded = rle_encode(sample_text)
    print(encoded)