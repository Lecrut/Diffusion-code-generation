WORD_LIST = {
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon"
}

def word_exists(word_set, search_word):
    return search_word in word_set

if __name__ == '__main__':
    search_term = "banana"
    result = word_exists(WORD_LIST, search_term)
    print(result)