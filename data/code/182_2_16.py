CHAR_LIST_SLICE = slice(None)

def string_to_char_list(s):
    return s[CHAR_LIST_SLICE]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    char_list = string_to_char_list(sample_string)
    print(char_list)