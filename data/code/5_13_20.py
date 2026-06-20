def capitalize_first(text):
    return text[:1].upper() + text[1:] if text else text

if __name__ == '__main__':
    sample = 'hello world'
    print(capitalize_first(sample))