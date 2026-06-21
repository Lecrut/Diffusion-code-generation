if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry")
    search_word = "banana"
    result = any(word == search_word for word in sample_tuple)
    print(result)