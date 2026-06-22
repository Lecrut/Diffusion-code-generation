def rle_encode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count = 1
        current_char = s[i]
        i += 1
        while i < len(s) and s[i] == current_char:
            count += 1
            i += 1
        result.append(current_char + str(count))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "AABBCC"
    encoded_result = rle_encode(sample_input)
    print(encoded_result)