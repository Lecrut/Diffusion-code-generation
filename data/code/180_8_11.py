def is_word_in_collection(word, collection):
    return any(word == item for item in collection)

if __name__ == '__main__':
    search_term = 'banana'
    fruit_basket = ['apple', 'orange', 'banana', 'grape']
    if is_word_in_collection(search_term, fruit_basket):
        print(f"'{search_term}' found in the basket.")
    else:
        print(f"'{search_term}' not found in the basket.")