def check_word_presence(word_list, text):
    for word in word_list:
        if word in text:
            return True
    return False
if __name__ == '__main__':
    words = ["apple", "banana", "cherry"]
    sentence = "I like to eat an apple and a banana."
    result = check_word_presence(words, sentence)
    print(result)