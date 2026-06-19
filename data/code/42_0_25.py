def concatenate_strings(string_list, delimiter):
    def join_with_delimiter(lst, sep):
        return sep.join(lst)
    
    return join_with_delimiter(string_list, delimiter)

if __name__ == '__main__':
    sample_strings = ["red", "green", "blue"]
    separator = " | "
    combined_string = concatenate_strings(sample_strings, separator)
    print(combined_string)