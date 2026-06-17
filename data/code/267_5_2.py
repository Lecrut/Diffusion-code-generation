def check_long_words(string_iterable):
    for word in string_iterable:
        if len(word) > 10:
            yield word
if __name__ == '__main__':
    sample_data = ["short", "longerword", "thisisalongword", "medium", "verylongwordexample"]
    result_generator = check_long_words(sample_data)
    result_list = list(result_generator)
    print(result_list)