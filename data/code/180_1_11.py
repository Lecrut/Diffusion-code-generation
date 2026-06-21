def word_in_text(target_word, text):
    words = set(text.split())
    return target_word in words

if __name__ == '__main__':
    target = "python"
    text1 = "This is a sample text about python programming."
    text2 = "This text does not contain the word python."
    text3 = "Python is fun."
    text4 = "programming"
    print(f"'{target}' in '{text1}': {word_in_text(target, text1)}")
    print(f"'{target}' in '{text2}': {word_in_text(target, text2)}")
    print(f"'{target}' in '{text3}': {word_in_text(target, text3)}")
    print(f"'{target}' in '{text4}': {word_in_text(target, text4)}")