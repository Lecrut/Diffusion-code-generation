def manipulate_case(input_string):
    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    TITLE_CASED = 'title_cased'

    def to_lowercase(s):
        return s.lower()

    def to_uppercase(s):
        return s.upper()

    def to_title_case(s):
        return s.title()

    results = {
        LOWERCASE: to_lowercase(input_string),
        UPPERCASE: to_uppercase(input_string),
        TITLE_CASED: to_title_case(input_string)
    }
    return results

if __name__ == '__main__':
    SAMPLE_INPUT = "Hello World Example"
    RESULT = manipulate_case(SAMPLE_INPUT)
    print(RESULT)