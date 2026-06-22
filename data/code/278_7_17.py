SAMPLE_STRING = 'hello'

def print_unicode_chars(string):
    for char in string:
        print(f'Character: {char}, Unicode Code Point: {ord(char)}')
if __name__ == '__main__':
    print_unicode_chars(SAMPLE_STRING)