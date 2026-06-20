def capitalize_words(words):
    result = []
    for word in words:
        capitalized_word = word.capitalize()
        result.append(capitalized_word)
    return result

if __name__ == '__main__':
    sample_words = ["hello", "world", "python", "programming"]
    capitalized_words = capitalize_words(sample_words)
    print(capitalized_words)