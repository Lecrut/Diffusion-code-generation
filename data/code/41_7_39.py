def format_string(s):
    ORIGINAL_INDEX = 0
    ALL_CAPS_INDEX = 1
    SENTENCE_CASE_INDEX = 2

    def convert_to_all_caps(input_str):
        return input_str.upper()

    def convert_to_sentence_case(input_str):
        return input_str.capitalize()
    results = [s, convert_to_all_caps(s), convert_to_sentence_case(s)]
    return f'{results[ORIGINAL_INDEX]}, {results[ALL_CAPS_INDEX]}, {results[SENTENCE_CASE_INDEX]}'
if __name__ == '__main__':
    sample_input = 'hello world'
    formatted_output = format_string(sample_input)
    print(formatted_output)