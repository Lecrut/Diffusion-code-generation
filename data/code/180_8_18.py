def is_word_in_collection(word, collection):
    return any(word == item for item in collection)

if __name__ == '__main__':
    search_term = 'banana'
    fruit_basket = ['apple', 'orange', 'banana', 'grape']
    print(is_word_in_collection(search_term, fruit_basket))