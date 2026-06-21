def int_to_word(num):
    if not isinstance(num, int):
        raise TypeError('Input must be an integer')
    word_map = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    if num in word_map:
        return word_map[num]
    else:
        raise ValueError('Number out of range')
if __name__ == '__main__':
    print(int_to_word(5))
    print(int_to_word(10))