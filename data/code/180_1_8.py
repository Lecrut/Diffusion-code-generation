def word_present(target_word, text):
    return target_word in text
if __name__ == '__main__':
    word = "hello"
    text = "this is a test sentence for hello world"
    result = word_present(word, text)
    print(result)
    word = "python"
    text = "this is a test sentence for hello world"
    result = word_present(word, text)
    print(result)
    word = "java"
    text = "this is a test sentence for hello world"
    result = word_present(word, text)
    print(result)