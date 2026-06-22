def run_length_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(f"{count}{text[i - 1]}")
            count = 1
    result.append(f"{count}{text[-1]}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaaaabbbccccddddd"
    encoded_sample = run_length_encode(sample_text)
    print(encoded_sample)
    unicode_text = "🎉🎉🎉🎉🎉😀😀😎😎😎"
    encoded_unicode = run_length_encode(unicode_text)
    print(encoded_unicode)