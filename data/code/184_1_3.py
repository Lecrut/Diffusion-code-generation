def check_word_presence(text, target):
    text_lower = text.lower()
    target_lower = target.lower()
    return target_lower in text_lower
if __name__ == '__main__':
    string1 = "Hello World"
    word1 = "world"
    result1 = check_word_presence(string1, word1)
    print(f"'{word1}' in '{string1}': {result1}")
    string2 = "Programming is Fun"
    word2 = "proGramming"
    result2 = check_word_presence(string2, word2)
    print(f"'{word2}' in '{string2}': {result2}")
    string3 = "Python"
    word3 = "java"
    result3 = check_word_presence(string3, word3)
    print(f"'{word3}' in '{string3}': {result3}")
    string4 = "Apple Banana Orange"
    word4 = "apple"
    result4 = check_word_presence(string4, word4)
    print(f"'{word4}' in '{string4}': {result4}")