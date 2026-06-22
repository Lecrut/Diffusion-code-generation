def contains_special_char(text):
    special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '='}
    return bool(set(text) & special_chars)

if __name__ == '__main__':
    result = contains_special_char("Hello World!")
    print(result)