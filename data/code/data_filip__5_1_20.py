def capitalize_first_characters(strings):
    result = []
    for s in strings:
        if not s:
            result.append(s)
        else:
            result.append(s[0].upper() + s[1:])
    return result

if __name__ == '__main__':
    sample_list = ["hello", "world", "", "python", "list"]
    print(capitalize_first_characters(sample_list))