def is_word_present(word_list, word):
    if not isinstance(word_list, list) or not all(isinstance(item, str) for item in word_list):
        raise ValueError("word_list must be a list of strings")
    if not isinstance(word, str):
        raise ValueError("word must be a string")

    word_set = set(word_list)
    return word.lower() in word_set

if __name__ == '__main__':
    word_list1 = ["apple", "banana", "cherry"]
    word1 = "Banana"
    print(f"'{word1}' in {word_list1}: {is_word_present(word_list1, word1)}")

    word_list2 = ["python", "programming", "code"]
    word2 = "Python"
    print(f"'{word2}' in {word_list2}: {is_word_present(word_list2, word2)}")

    word_list3 = ["case", "sensitivity", "test"]
    word3 = "Case"
    print(f"'{word3}' in {word_list3}: {is_word_present(word_list3, word3)}")

    word_list4 = ["example", "text", "data"]
    word4 = "missing"
    print(f"'{word4}' in {word_list4}: {is_word_present(word_list4, word4)}")