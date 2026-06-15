def word_exists(word_list, text):
    for word in word_list:
        if word in text:
            return True
    return False
if __name__ == '__main__':
    words = ["apple", "banana", "cherry"]
    sentence = "I like apple and banana today."
    result = word_exists(words, sentence)
    print(result)