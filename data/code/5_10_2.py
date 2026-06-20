def capitalize_words(words):
    return [word.capitalize() for word in words]

if __name__ == '__main__':
    sample_words = ["hello", "world", "python", "code"]
    result = capitalize_words(sample_words)
    print(result)