def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == "__main__":
    sample_text = "aaaaaabbbcccddeeeefffff"
    result = run_length_encode(sample_text)
    print(result)
    unicode_text = "你好你好你好世界世界"
    unicode_result = run_length_encode(unicode_text)
    print(unicode_result)