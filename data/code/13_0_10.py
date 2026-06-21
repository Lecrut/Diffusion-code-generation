def snake_to_camel(s: str) -> str:
    parts = s.split('_')
    return parts[0] + ''.join((word.capitalize() for word in parts[1:]))
if __name__ == '__main__':
    test_cases = ['hello_world', 'this_is_snake_case', 'alreadycamel', 'single_word', 'multiple_words_here', 'leading_underscore', '_trailing_underscore', 'a_b_c_d_e', 'snake_case_to_camel_case', 'no_underscores', '___multiple___underscores___']
    for test in test_cases:
        result = snake_to_camel(test)
        print(f'{test} -> {result}')