if __name__ == '__main__':
    words_tuple = ("apple", "banana", "cherry", "date")
    search_word = "banana"
    
    result = any(word == search_word for word in words_tuple)
    
    print(result)