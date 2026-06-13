def word_present(target_word, text):
    return target_word in text
if __name__ == '__main__':
    target = "hello"
    text1 = "this is a test sentence"
    text2 = "hello world"
    text3 = "testing hello"
    text4 = "no match here"
    print(f"'{target}' in '{text1}': {word_present(target, text1)}")
    print(f"'{target}' in '{text2}': {word_present(target, text2)}")
    print(f"'{target}' in '{text3}': {word_present(target, text3)}")
    print(f"'{target}' in '{text4}': {word_present(target, text4)}")