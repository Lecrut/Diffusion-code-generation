def filter_non_unique_chars(text):
    if not text:
        return ""
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    result_chars = []
    seen = set()
    for char in text:
        if char_count[char] > 1 and char not in seen:
            result_chars.append(char)
            seen.add(char)
    return "".join(result_chars)

if __name__ == '__main__':
    sample_string = "programming"
    result = filter_non_unique_chars(sample_string)
    print(result)