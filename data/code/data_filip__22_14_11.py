def compress_rle(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

def compare_and_return_optimal(s):
    if not s:
        return s
    compressed = compress_rle(s)
    if len(compressed) < len(s):
        return compressed
    return s

if __name__ == "__main__":
    sample_strings = ["aaabbbcccc", "abc", "wwwwwwwwww", "a1b2c3"]
    for test in sample_strings:
        result = compare_and_return_optimal(test)
        print(f"Input: {test} -> Output: {result}")