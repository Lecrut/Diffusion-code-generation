CONST_SPACE = ' '
CONST_UNDERSCORE = '_'

def replace_spaces_with_underscores(input_string):
    parts = input_string.split(CONST_SPACE)
    joined_result = CONST_UNDERSCORE.join(parts)
    return joined_result

if __name__ == '__main__':
    sample_input = "foo bar baz qux"
    output_value = replace_spaces_with_underscores(sample_input)
    print(output_value)