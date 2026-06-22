def capitalize_words(words):
    return [word.capitalize() if word else word for word in words]

if __name__ == '__main__':
    sample_input = ["hello", "world", "", "python"]
    result = capitalize_words(sample_input)
    print(result)