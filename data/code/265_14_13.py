def are_char_sets_equal(phrase1: str, phrase2: str) -> bool:
    return set(phrase1) == set(phrase2)
if __name__ == '__main__':
    print(are_char_sets_equal('listen', 'silent'))
    print(are_char_sets_equal('hello', 'world'))
    print(are_char_sets_equal('binary', 'brainy'))
    print(are_char_sets_equal('apple', 'papel'))
    print(are_char_sets_equal('rat', 'car'))