def to_camel_case(snake_string: str) -> str:
    parts = snake_string.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_snake = 'this_is_a_test_string'
    result = to_camel_case(sample_snake)
    print(result)
    another_sample = 'another_example'
    another_result = to_camel_case(another_sample)
    print(another_result)
    empty_sample = ''
    empty_result = to_camel_case(empty_sample)
    print(empty_result)
    single_word = 'only_one'
    single_result = to_camel_case(single_word)
    print(single_result)