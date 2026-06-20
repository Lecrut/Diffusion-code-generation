def capitalize_words(words: list[str]) -> list[str]:
    return [word.capitalize() if word else word for word in words]

if __name__ == '__main__':
    sample_words = ["hello", "world", "python", ""]
    result = capitalize_words(sample_words)
    print(result)