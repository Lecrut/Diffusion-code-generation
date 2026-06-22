def has_unique_characters(text):
    return len(text) == len(set(text))

if __name__ == '__main__':
    sample_text = "abcdefg"
    result = has_unique_characters(sample_text)
    print(result)