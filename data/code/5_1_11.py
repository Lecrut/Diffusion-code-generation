def capitalize_first(strings):
    result = []
    for s in strings:
        if len(s) > 0:
            result.append(s[0].upper() + s[1:])
        else:
            result.append(s)
    return result

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "", "data"]
    print(capitalize_first(sample_strings))