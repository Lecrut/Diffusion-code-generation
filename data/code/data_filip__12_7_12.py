import re

def process_string(input_string: str) -> str:
    if input_string is None:
        raise ValueError('Input string cannot be None')
    stripped = input_string.strip()
    if not stripped:
        raise ValueError('Input string is empty after stripping')
    chars_to_keep = set()
    for c in stripped:
        if c.isdigit() or c == '-' or c == '+':
            chars_to_keep.add(c)
    table = {}
    for i in range(65536):
        c = chr(i)
        if c in stripped and c not in ['-', '+'] and (not c.isdigit()):
            table[i] = None
        elif c in ['-', '+'] and c not in stripped:
            table[i] = None
        elif c.isdigit() and c not in stripped:
            table[i] = None
        else:
            table[i] = i
    keep_chars = set('0123456789-+')
    trans_table = {}
    for i in range(65536):
        c = chr(i)
        if c in keep_chars:
            trans_table[i] = i
        else:
            trans_table[i] = None
    cleaned = stripped.translate(trans_table)
    if not re.match('^[+-]?\\d+$', cleaned):
        raise ValueError(f"Cleaned string '{cleaned}' does not consist solely of integers")
    if not cleaned:
        raise ValueError('Cleaned string is empty')
    int_value = int(cleaned)
    return str(int_value)
if __name__ == '__main__':
    test_string = '  -1,234.56  '
    result = process_string(test_string)
    print(result)