CODE_TO_WORD = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

def get_word_from_code(code):
    try:
        return CODE_TO_WORD[code]
    except KeyError:
        raise ValueError(f'Invalid code: {code}')
if __name__ == '__main__':
    sample_codes = [1, 2, 3, 4, 5, 6]
    for code in sample_codes:
        try:
            word = get_word_from_code(code)
            print(f'Code {code}: {word}')
        except ValueError as e:
            print(e)