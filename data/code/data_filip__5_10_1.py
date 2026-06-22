def capitalize_words(words):
    capitalized = []
    for word in words:
        capitalized.append(word.capitalize())
    return capitalized

if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "programming"]
    result = capitalize_words(sample_list)
    print(result)