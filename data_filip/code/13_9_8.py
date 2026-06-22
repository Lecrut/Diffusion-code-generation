def snake_to_camel(snake_case_str: str) -> str:
    if not snake_case_str:
        return ""
    parts = snake_case_str.split('_')
    first_word = parts[0]
    remaining_words = parts[1:]
    capitalized_words = [word.capitalize() for word in remaining_words if word]
    return first_word + ''.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "this_is_a_test_string"
    result = snake_to_camel(sample_input)
    print(result)