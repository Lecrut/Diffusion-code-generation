def int_to_word(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError('Input must be a non-negative integer')
    word_map = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    if num in word_map:
        return word_map[num]
    else:
        raise KeyError('Number not mapped to a word')
if __name__ == '__main__':
    print(int_to_word(5))
    print(int_to_word(0))