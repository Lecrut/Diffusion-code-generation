def word_present(target_word, text):
    return target_word in text
if __name__ == '__main__':
    word1 = "apple"
    text1 = "I like apple and banana"
    print(f"'{word1}' in '{text1}': {word_present(word1, text1)}")
    word2 = "orange"
    text2 = "I like apple and banana"
    print(f"'{word2}' in '{text2}': {word_present(word2, text2)}")
    word3 = "apple"
    text3 = "apple"
    print(f"'{word3}' in '{text3}': {word_present(word3, text3)}")
    word4 = "cat"
    text4 = "apple and banana"
    print(f"'{word4}' in '{text4}': {word_present(word4, text4)}")