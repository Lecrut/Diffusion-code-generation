def generate_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            yield s[i:j+1]
if __name__ == '__main__':
    test_string = "abc"
    substring_generator = generate_substrings(test_string)
    result_list = list(substring_generator)
    print(result_list)
    test_string_2 = "a"
    substring_generator_2 = generate_substrings(test_string_2)
    result_list_2 = list(substring_generator_2)
    print(result_list_2)
    test_string_3 = "ab"
    substring_generator_3 = generate_substrings(test_string_3)
    result_list_3 = list(substring_generator_3)
    print(result_list_3)