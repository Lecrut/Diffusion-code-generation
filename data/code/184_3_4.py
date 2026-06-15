def check_word_presence(list_of_strings, target_word):
    result_dict = {}
    for s in list_of_strings:
        result_dict[s] = target_word in s
    return result_dict
if __name__ == '__main__':
    sample_strings = ["hello world", "python programming", "a simple test", "this is a test"]
    target = "test"
    output = check_word_presence(sample_strings, target)
    print(output)