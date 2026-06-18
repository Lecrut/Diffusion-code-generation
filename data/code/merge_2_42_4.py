def sort_words(words):
    return sorted(words, key=lambda x: x.lower())
if __name__ == '__main__':
    words = ["Python", "apple", "Banana", "cherry"]
    print(sort_words(words))