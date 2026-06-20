def capitalize_first_chars(strings):
    result = []
    for s in strings:
        if s:
            result.append(s[0].upper() + s[1:])
        else:
            result.append(s)
    return result

if __name__ == '__main__':
    sample_input = ['hello', 'WORLD', '', 'test', 'another']
    result = capitalize_first_chars(sample_input)
    print(result)