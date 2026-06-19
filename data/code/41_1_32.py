def manipulate_case(input_string):
    LOWERCASE_KEY = "lowercase"
    UPPERCASE_KEY = "uppercase"
    TITLE_CASE_KEY = "title_case"

    lowercase_str = input_string.lower()
    uppercase_str = input_string.upper()
    title_cased_str = str(input_string).title()

    result_dict = {
        LOWERCASE_KEY: lowercase_str,
        UPPERCASE_KEY: uppercase_str,
        TITLE_CASE_KEY: title_cased_str
    }
    return result_dict

if __name__ == '__main__':
    sample_input = "Optimize This String"
    result = manipulate_case(sample_input)
    print(result)