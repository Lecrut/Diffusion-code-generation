def reverse_sentence_in_place(sentence):
    def reverse_word(word):
        return word[::-1]
    
    words = sentence.split()
    reversed_words = [reverse_word(word) for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

if __name__ == '__main__':
    test_sentence = 'Python is fun and powerful'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)