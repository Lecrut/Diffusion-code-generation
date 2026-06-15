def check_word_presence(text, target):
    text_lower = text.lower()
    target_lower = target.lower()
    return target_lower in text_lower
if __name__ == '__main__':
    text1 = "Hello World"
    word1 = "world"
    print(f"'{word1}' in '{text1}': {check_word_presence(text1, word1)}")
    text2 = "Python Programming"
    word2 = "python"
    print(f"'{word2}' in '{text2}': {check_word_presence(text2, word2)}")
    text3 = "Case Sensitivity Test"
    word3 = "sensitivity"
    print(f"'{word3}' in '{text3}': {check_word_presence(text3, word3)}")
    text4 = "Example Text"
    word4 = "missing"
    print(f"'{word4}' in '{text4}': {check_word_presence(text4, word4)}")