def is_word_present(text, word):
    return word.lower() in text.lower()
if __name__ == '__main__':
    text1 = "Hello World"
    word1 = "world"
    print(f"'{word1}' in '{text1}': {is_word_present(text1, word1)}")
    text2 = "Python Programming"
    word2 = "python"
    print(f"'{word2}' in '{text2}': {is_word_present(text2, word2)}")
    text3 = "Case Sensitivity Test"
    word3 = "case"
    print(f"'{word3}' in '{text3}': {is_word_present(text3, word3)}")
    text4 = "No Match Here"
    word4 = "match"
    print(f"'{word4}' in '{text4}': {is_word_present(text4, word4)}")