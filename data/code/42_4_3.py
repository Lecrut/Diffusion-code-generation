def concatenate_with_separator(string_iterable, separator):
    result = ""
    for s in string_iterable:
        result += s + separator
    yield result.rstrip(separator)
if __name__ == '__main__':
    input_strings = ["apple", "banana", "cherry"]
    custom_separator = ", "
    generator = concatenate_with_separator(input_strings, custom_separator)
    output = "".join(generator)
    print(output)