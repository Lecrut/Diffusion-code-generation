def capitalize_words(words):
    capitalized = []
    for word in words:
        if word:
            capitalized.append(word[0].upper() + word[1:])
        else:
            capitalized.append(word)
    return capitalized

if __name__ == '__main__':
    sample_words = ["hello", "world", "python", ""]
    result = capitalize_words(sample_words)
    print(result)