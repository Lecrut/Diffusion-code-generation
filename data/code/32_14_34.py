def get_phrase_length(input_string):
    return len(input_string.strip())
if __name__ == '__main__':
    print(get_phrase_length('Hello, World!'))
    print(get_phrase_length('   '))
    print(get_phrase_length(''))
    print(get_phrase_length('Python\n'))