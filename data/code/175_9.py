def split_by_space(text):
    parts = []
    current_part = ""
    for char in text:
        if char == ' ':
            if current_part:
                parts.append(current_part)
                current_part = ""
        else:
            current_part += char
    if current_part:
        parts.append(current_part)
    return parts
if __name__ == '__main__':
    sample_text1 = "this is a test string"
    result1 = split_by_space(sample_text1)
    print(result1)
    sample_text2 = "multiple   spaces here"
    result2 = split_by_space(sample_text2)
    print(result2)
    sample_text3 = "singleword"
    result3 = split_by_space(sample_text3)
    print(result3)
    sample_text4 = " leading space"
    result4 = split_by_space(sample_text4)
    print(result4)