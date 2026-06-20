def capitalize_words(strings):
    return [word.capitalize() for word in strings]

if __name__ == '__main__':
    sample_input = ["hello", "world", "python"]
    result = capitalize_words(sample_input)
    print(result)