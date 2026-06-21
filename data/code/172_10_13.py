def map_int_to_word(num):
    word_map = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    return word_map.get(num, 'unknown')
if __name__ == '__main__':
    print(map_int_to_word(3))
    print(map_int_to_word(10))