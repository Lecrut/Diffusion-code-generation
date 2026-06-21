if __name__ == '__main__':
    words_tuple = ("apple", "banana", "cherry")
    search_word = "banana"
    result = any(word in words_tuple for word in [search_word])
    print(result)