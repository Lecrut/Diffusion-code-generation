def is_word_present(text, word):
    return word.lower() in text.lower()
if __name__ == '__main__':
    string1 = "Hello World"
    word1 = "world"
    print(f"'{word1}' in '{string1}': {is_word_present(string1, word1)}")
    string2 = "Python Programming"
    word2 = "python"
    print(f"'{word2}' in '{string2}': {is_word_present(string2, word2)}")
    string3 = "Case Insensitivity Test"
    word3 = "case"
    print(f"'{word3}' in '{string3}': {is_word_present(string3, word3)}")
    string4 = "Example Text"
    word4 = "missing"
    print(f"'{word4}' in '{string4}': {is_word_present(string4, word4)}")