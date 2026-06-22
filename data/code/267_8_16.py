def is_word_long(word):
    length_map = {1: False, 2: False, 3: False, 4: False, 5: False, 6: True, 7: True, 8: True, 9: True, 10: True}
    return length_map.get(len(word), False)
if __name__ == '__main__':
    print(is_word_long('test'))
    print(is_word_long('testing'))