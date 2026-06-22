def convert_to_cases(input_text):
    LOWERCASE = 'lower'
    UPPERCASE = 'upper'
    TITLECASE = 'title'

    def apply_case(text, case_type):
        if case_type == LOWERCASE:
            return text.lower()
        elif case_type == UPPERCASE:
            return text.upper()
        elif case_type == TITLECASE:
            return text.title()
        else:
            raise ValueError("Invalid case type")

    lowercase_text = apply_case(input_text, LOWERCASE)
    uppercase_text = apply_case(input_text, UPPERCASE)
    titlecase_text = apply_case(input_text, TITLECASE)

    return lowercase_text, uppercase_text, titlecase_text

if __name__ == '__main__':
    SAMPLE_TEXT = "Transform This String to Different Cases"
    lower, upper, title = convert_to_cases(SAMPLE_TEXT)
    print(lower)
    print(upper)
    print(title)