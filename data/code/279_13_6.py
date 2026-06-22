CHARS_TO_PRINT = {'Python': list('Python')}

def print_chars(s):
    if s not in CHARS_TO_PRINT:
        raise ValueError("Input must be 'Python'")
    for char in CHARS_TO_PRINT[s]:
        print(char)

if __name__ == '__main__':
    try:
        print_chars('Python')
    except ValueError as e:
        print(e)