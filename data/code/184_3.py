def check_word_presence(list_of_strings, target_word):
    result_dict = {}
    for s in list_of_strings:
        result_dict[s] = target_word in s
    return result_dict
if __name__ == '__main__':
    sample_list = ["hello world", "python programming", "this is a test", "world"]
    target = "world"
    output = check_word_presence(sample_list, target)
    print(output)