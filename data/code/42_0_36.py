DELIMITER = ", "

def concatenate_strings(string_list, delimiter=DELIMITER):
    result = []
    for string in string_list:
        result.append(string)
    return delimiter.join(result)

if __name__ == '__main__':
    sample_strings = ["red", "green", "blue"]
    combined_string = concatenate_strings(sample_strings)
    print(combined_string)