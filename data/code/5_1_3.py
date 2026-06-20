def capitalize_first_chars(strings):
    result = []
    for s in strings:
        if not s:
            result.append(s)
        else:
            result.append(s[0].upper() + s[1:])
    return result

if __name__ == '__main__':
    sample = ["hello", "world", "", "python", "test"]
    print(capitalize_first_chars(sample))