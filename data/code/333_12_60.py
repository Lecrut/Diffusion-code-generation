def extract_first_letters(words):
    return [word[0].upper() for word in words]
if __name__ == '__main__':
    sample_input = ["hello", "world", "python", "programming"]
    result = extract_first_letters(sample_input)
    print("".join(result))