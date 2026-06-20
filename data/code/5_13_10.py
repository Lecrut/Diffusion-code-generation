def capitalize_first(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample = "hello world"
    result = capitalize_first(sample)
    print(result)