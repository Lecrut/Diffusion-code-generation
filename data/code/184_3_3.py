def check_word_presence(list_of_strings, target_word):
    result_dict = {}
    for text in list_of_strings:
        result_dict[text] = target_word in text
    return result_dict
if __name__ == '__main__':
    sample_list = ["hello world", "python programming", "a simple test", "this is not it"]
    target = "world"
    output = check_word_presence(sample_list, target)
    print(output)