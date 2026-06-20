def split_and_strip_tokens(text):
    return [token.strip() for token in text.split(',')]

if __name__ == '__main__':
    sample_string = "apple,  banana ,  cherry  , date"
    result = split_and_strip_tokens(sample_string)
    print(result)