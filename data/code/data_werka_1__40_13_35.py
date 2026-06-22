def get_first_alpha_character(s):
    ALPHABETIC_CHARS = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for char in s:
        if char in ALPHABETIC_CHARS:
            return char
    return None
if __name__ == '__main__':
    sample_strings = ['123abc456', 'hello world!', '', 'no alpha', '!@#']
    results = [get_first_alpha_character(s) for s in sample_strings]
    print(results)