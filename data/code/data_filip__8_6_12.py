COMMA_DELIM = ','

WHITESPACE = ' \t\n\r'

def extract_clean_parts(text):
    raw_segments = text.split(COMMA_DELIM)
    cleaned_parts = []
    for segment in raw_segments:
        stripped = segment.strip(WHITESPACE)
        if stripped:
            cleaned_parts.append(stripped)
    return cleaned_parts

if __name__ == '__main__':
    test_input_1 = "  red , green,  , blue,  "
    test_input_2 = ",,,,"
    test_input_3 = "single_item"
    test_input_4 = ""
    test_input_5 = "  ,  ,  "
    print(extract_clean_parts(test_input_1))
    print(extract_clean_parts(test_input_2))
    print(extract_clean_parts(test_input_3))
    print(extract_clean_parts(test_input_4))
    print(extract_clean_parts(test_input_5))