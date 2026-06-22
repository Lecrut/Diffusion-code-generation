def split_and_strip(text):
    return [token.strip() for token in text.split(',')]

if __name__ == '__main__':
    result = split_and_strip("  apple, banana ,cherry ,date ")
    print(result)