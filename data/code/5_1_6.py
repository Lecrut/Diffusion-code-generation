def capitalize_first_chars(strings):
    result = []
    for s in strings:
        if len(s) == 0:
            result.append("")
        else:
            result.append(s[0].upper() + s[1:])
    return result

if __name__ == '__main__':
    sample_data = ["hello", "world", "", "test", "a"]
    transformed = capitalize_first_chars(sample_data)
    print(transformed)