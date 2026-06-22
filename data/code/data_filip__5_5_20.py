def capitalize_first(s):
    return [s[0].upper()] + list(s[1:]) if s else []

if __name__ == '__main__':
    sample = "hello world"
    result = capitalize_first(sample)
    print(''.join(result))