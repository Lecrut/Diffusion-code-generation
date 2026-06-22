def has_unique_chars(text):
    if not text:
        return True
    sorted_text = sorted(text)
    for i in range(len(sorted_text) - 1):
        if sorted_text[i] == sorted_text[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "abcde"]
    results = {}
    for s in sample_strings:
        results[s] = has_unique_chars(s)
    for key in results:
        print(f"{key}: {results[key]}")