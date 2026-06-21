class StringSearch:
    @staticmethod
    def contains_word(sentence, word):
        return any(word in phrase for phrase in sentence)

if __name__ == '__main__':
    sample_sentence = ("apple", "banana", "cherry")
    search_word = "banana"
    result = StringSearch.contains_word(sample_sentence, search_word)
    print(result)