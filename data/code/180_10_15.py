word_set = {'apple', 'banana', 'cherry'}

def is_word_present(word_list, word):
    return word.lower() in word_set

if __name__ == '__main__':
    string1 = "Hello World"
    word1 = "world"
    print(f"'{word1}' in '{string1}': {is_word_present([word1], word1)}")
    string2 = "Python Programming"
    word2 = "python"
    print(f"'{word2}' in '{string2}': {is_word_present([word2], word2)}")
    string3 = "Case Sensitivity Test"
    word3 = "case"
    print(f"'{word3}' in '{string3}': {is_word_present([word3], word3)}")
    string4 = "No Match Here"
    word4 = "match"
    print(f"'{word4}' in '{string4}': {is_word_present([word4], word4)}")