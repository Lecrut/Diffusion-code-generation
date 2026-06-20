import re

_special_char_re = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_chars(s):
    return bool(_special_char_re.search(s))

if __name__ == '__main__':
    samples = [
        "Hello World",
        "Hello@World",
        "12345",
        "test string with !special chars.",
        "no special here",
        "spaces   and   tabs\tare okay",
        "",
        "!@#$%"
    ]
    for sample in samples:
        print(contains_special_chars(sample))