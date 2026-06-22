import re

_SPECIAL_CHAR_RE = re.compile(r'[^\w\s]')

def contains_special_characters(s):
    return bool(_SPECIAL_CHAR_RE.search(s))

if __name__ == '__main__':
    samples = ['hello', 'hello!', 'world@123', 'normal text', 'special#chars', '']
    for sample in samples:
        result = contains_special_characters(sample)
        print(f'{sample!r}: {result}')