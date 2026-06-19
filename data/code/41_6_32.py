def convert_to_title_case(strings):
    title_cased_list = []
    for string in strings:
        title_cased_string = string.title()
        title_cased_list.append(title_cased_string)
    return title_cased_list

if __name__ == '__main__':
    sample_strings = ["the quick brown fox", "jumps OVER the lazy dog", "PYTHON is FUN"]
    result = convert_to_title_case(sample_strings)
    print(result)