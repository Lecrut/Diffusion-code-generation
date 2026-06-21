def run_length_encode(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_texts = ["AABBBCC", "ABC", "AAAAAAAA", "A", "", "XXYZ"]
    for text in sample_texts:
        print(run_length_encode(text))