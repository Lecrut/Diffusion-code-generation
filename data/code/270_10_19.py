def remove_spaces_in_list(string_list):
    return [s.replace(' ', '') for s in string_list]

if __name__ == '__main__':
    sample_strings = ["Hello World", "Python Programming", "Remove Spaces"]
    processed_strings = remove_spaces_in_list(sample_strings)
    print(processed_strings)