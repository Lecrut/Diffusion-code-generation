def is_word_in_collection(word, collection):
    return any(word == item for item in collection)

if __name__ == '__main__':
    search_term = 'banana'
    fruits = ['apple', 'banana', 'cherry', 'date']
    result = is_word_in_collection(search_term, fruits)
    print(result)