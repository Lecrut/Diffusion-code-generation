def capitalize_words(word_list):
    capitalized = []
    for word in word_list:
        capitalized.append(word.capitalize())
    return capitalized

if __name__ == '__main__':
    sample_words = ["hello", "world", "python"]
    result = capitalize_words(sample_words)
    print(result)