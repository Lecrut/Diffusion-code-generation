if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry")
    word_to_find = "banana"
    result = any(word in sample_tuple for word in (word_to_find,))
    print(result)