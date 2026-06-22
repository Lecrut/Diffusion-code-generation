def concatenate_strings(strings, delimiter):
    return delimiter.join(strings)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    delimiter = ", "
    result = concatenate_strings(sample_strings, delimiter)
    print(result)