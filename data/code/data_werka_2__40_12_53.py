def extract_first_alpha(s):
    ALPHABETIC_CHARS = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for char in s:
        if char in ALPHABETIC_CHARS:
            return char
    raise ValueError('No alphabetic character found')
if __name__ == '__main__':
    sample_values = ['123abc', '!@#456def', '   ghi', '7890', '', 'noalpha123', 'anotherTest!@#']
    for value in sample_values:
        try:
            print(extract_first_alpha(value))
        except ValueError as e:
            print(e)