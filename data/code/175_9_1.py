def custom_split(text):
    result = []
    start = 0
    for i in range(len(text)):
        if text[i] == ' ':
            if i > start:
                result.append(text[start:i])
                start = i + 1
        elif i == len(text) - 1:
            if start < i:
                result.append(text[start:i+1])
        else:
            continue
    if start < len(text):
        result.append(text[start:])
    return result
if __name__ == '__main__':
    sample_text = "this is a test string"
    separated_words = custom_split(sample_text)
    print(separated_words)