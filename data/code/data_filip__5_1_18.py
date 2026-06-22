def capitalize_first_char(strings):
    result = []
    for s in strings:
        if s:
            result.append(s[0].upper() + s[1:])
        else:
            result.append(s)
    return result

if __name__ == '__main__':
    sample_input = ["hello", "world", "python", ""]
    output = capitalize_first_char(sample_input)
    print(output)