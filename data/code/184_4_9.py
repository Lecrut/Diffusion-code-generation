if __name__ == '__main__':
    words = ("apple", "banana", "cherry", "date")
    search_word = "banana"
    found = any(search_word in word for word in words)
    print(found)