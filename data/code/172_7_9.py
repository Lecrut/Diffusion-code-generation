CODE_TO_WORD = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

def get_word_from_code(code):
    return CODE_TO_WORD.get(code, 'unknown')
if __name__ == '__main__':
    sample_codes = [1, 2, 6, 3, 5]
    for code in sample_codes:
        word = get_word_from_code(code)
        print(f'Code {code}: {word}')