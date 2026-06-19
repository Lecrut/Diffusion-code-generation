def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]
if __name__ == '__main__':
    sample_input = 'hello world'
    result = capitalize_first_letter(sample_input)
    print(result)