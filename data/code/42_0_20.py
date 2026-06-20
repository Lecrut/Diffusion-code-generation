def concatenate_strings(strings, delimiter):
    if not strings:
        return ""
    result = strings[0]
    for i in range(1, len(strings)):
        result += delimiter
        result += strings[i]
    return result

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    sample_delimiter = ", "
    output = concatenate_strings(sample_strings, sample_delimiter)
    print(output)