CODE_TO_WORD = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

def get_word_from_code(code):
    return CODE_TO_WORD.get(code, 'unknown')
if __name__ == '__main__':
    print(get_word_from_code(5))
    print(get_word_from_code(10))