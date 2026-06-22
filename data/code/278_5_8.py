ascii_values = {'a': 97, 'b': 98, 'c': 99}

def print_ascii(char):
    if char in ascii_values:
        print(f'{char}: {ascii_values[char]}')
    else:
        print(f"Character '{char}' not found.")
if __name__ == '__main__':
    chars = ['a', 'b', 'c', 'd']
    for char in chars:
        print_ascii(char)