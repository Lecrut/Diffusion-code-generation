def word_present(target_word, text):
    return target_word in text
if __name__ == '__main__':
    target = "python"
    text = "This is a sample text about python programming."
    result = word_present(target, text)
    print(result)
    target = "java"
    text = "This is a sample text about python programming."
    result = word_present(target, text)
    print(result)
    target = "missing"
    text = "This is a sample text about python programming."
    result = word_present(target, text)
    print(result)