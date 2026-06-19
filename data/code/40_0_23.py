import re

def get_first_letters(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    words = re.split('\\s+', text.strip())
    first_letters = [word[0] for word in words]
    return ''.join(first_letters)
if __name__ == '__main__':
    sample_string_1 = '  Hello world, this is a test '
    sample_string_2 = 'multiple   spaces\tand\nnewlines'
    sample_string_3 = 'singleword'
    sample_string_4 = '   '
    sample_string_5 = ''
    try:
        print(f"Input: '{sample_string_1}'")
        print(get_first_letters(sample_string_1))
        print('-' * 20)
        print(f"Input: '{sample_string_2}'")
        print(get_first_letters(sample_string_2))
        print('-' * 20)
        print(f"Input: '{sample_string_3}'")
        print(get_first_letters(sample_string_3))
        print('-' * 20)
        print(f"Input: '{sample_string_4}'")
        print(get_first_letters(sample_string_4))
        print('-' * 20)
        print(f"Input: '{sample_string_5}'")
        print(get_first_letters(sample_string_5))
    except ValueError as e:
        print(e)