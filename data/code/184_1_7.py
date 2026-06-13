def check_word_presence(text, target):
    text_lower = text.lower()
    target_lower = target.lower()
    return target_lower in text_lower
if __name__ == '__main__':
    string1 = "Hello World"
    word1 = "world"
    result1 = check_word_presence(string1, word1)
    print(f"'{word1}' in '{string1}': {result1}")
    string2 = "Python Programming"
    word2 = "python"
    result2 = check_word_presence(string2, word2)
    print(f"'{word2}' in '{string2}': {result2}")
    string3 = "Case Sensitivity Test"
    word3 = "sensitivity"
    result3 = check_word_presence(string3, word3)
    print(f"'{word3}' in '{string3}': {result3}")
    string4 = "No Match Here"
    word4 = "present"
    result4 = check_word_presence(string4, word4)
    print(f"'{word4}' in '{string4}': {result4}")