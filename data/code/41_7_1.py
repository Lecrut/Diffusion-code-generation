def convert_to_title_case(string_list):
    title_cased_list = []
    for s in string_list:
        title_cased_list.append(s.title())
    return title_cased_list
if __name__ == '__main__':
    input_list = ["hello world", "python programming", "list comprehension", "optimization"]
    result = convert_to_title_case(input_list)
    print(result)