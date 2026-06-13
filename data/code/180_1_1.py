def word_present(target_word, text):
    return target_word in text
if __name__ == '__main__':
    word = "python"
    text = "This is a sample text about python programming."
    result = word_present(word, text)
    print(result)
    word = "java"
    text = "This is a sample text about python programming."
    result = word_present(word, text)
    print(result)
    word = "missing"
    text = "This is a sample text about python programming."
    result = word_present(word, text)
    print(result)