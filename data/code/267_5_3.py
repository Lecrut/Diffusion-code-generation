def check_long_words(string_iterable):
    for s in string_iterable:
        if len(s) > 10:
            yield s
if __name__ == '__main__':
    sample_data = ["short", "thisisalongword", "anotherone", "verylongwordexample", "medium"]
    result_generator = check_long_words(sample_data)
    result_list = list(result_generator)
    print(result_list)