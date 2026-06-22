def capitalize_first(strings):
    result = []
    for s in strings:
        if len(s) == 0:
            result.append(s)
        else:
            result.append(s[0].upper() + s[1:])
    return result

if __name__ == '__main__':
    sample_input = ["hello", "world", ""]
    output = capitalize_first(sample_input)
    print(output)