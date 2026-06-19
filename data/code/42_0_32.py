DELIMITER = ", "

def concatenate_strings(string_list, delimiter=DELIMITER):
    result = []
    for string in string_list:
        result.append(string)
    return delimiter.join(result)

if __name__ == '__main__':
    input_strings = ["red", "green", "blue", "yellow"]
    separator = "; "
    final_result = concatenate_strings(input_strings, separator)
    print(final_result)