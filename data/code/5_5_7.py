def capitalize_first_letter(s):
    if not s:
        return s
    return [s[0].upper()] + list(s[1:])

if __name__ == '__main__':
    sample = 'hello world'
    result = capitalize_first_letter(sample)
    print(''.join(result))