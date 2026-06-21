def int_to_word(num):
    words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    if isinstance(num, int) and 0 <= num < 10:
        return words[num]
    else:
        raise ValueError('Input must be an integer between 0 and 9')
if __name__ == '__main__':
    print(int_to_word(5))
    print(int_to_word(9))