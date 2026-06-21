CODE_TO_WORD = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

def validate_input(code):
    if not isinstance(code, int) or code not in CODE_TO_WORD:
        raise ValueError(f'Invalid input: {code}. Expected one of {list(CODE_TO_WORD.keys())}')

def get_word_from_code(code):
    validate_input(code)
    return CODE_TO_WORD[code]
if __name__ == '__main__':
    sample_codes = [1, 3, 5, 2, 4]
    for code in sample_codes:
        try:
            print(f'Code {code}: {get_word_from_code(code)}')
        except ValueError as e:
            print(e)