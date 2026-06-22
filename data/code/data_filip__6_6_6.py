def replace_internal_spaces(text):
    if not text:
        return text
    parts = text.split(' ')
    return '_'.join(parts)

if __name__ == '__main__':
    result = replace_internal_spaces('hello world foo bar')
    print(result)