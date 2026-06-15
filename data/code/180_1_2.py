def word_present(target_word, text):
    return target_word in text
if __name__ == '__main__':
    target = "python"
    text = "this is a sample text for python programming"
    result = word_present(target, text)
    print(result)
    target = "java"
    text = "this is a sample text for python programming"
    result = word_present(target, text)
    print(result)
    target = "missing"
    text = "this is a sample text for python programming"
    result = word_present(target, text)
    print(result)