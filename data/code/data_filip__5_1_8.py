def capitalize_first_chars(strings):
    result = []
    for s in strings:
        if len(s) == 0:
            result.append("")
        else:
            result.append(s[0].upper() + s[1:])
    return result

if __name__ == '__main__':
    sample_input = ["hello", "world", "", "python", "code", "a", ""]
    output = capitalize_first_chars(sample_input)
    print(output)