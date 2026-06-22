class StringFormatter:
    CASE_LOWER = 'lower'
    CASE_UPPER = 'upper'
    CASE_TITLE = 'title'

    @staticmethod
    def convert_case(text, case_type):
        if case_type == StringFormatter.CASE_LOWER:
            return text.lower()
        elif case_type == StringFormatter.CASE_UPPER:
            return text.upper()
        elif case_type == StringFormatter.CASE_TITLE:
            return text.title()
        else:
            raise ValueError("Invalid case type")

    def format_string(self, text):
        lowercase_text = self.convert_case(text, StringFormatter.CASE_LOWER)
        uppercase_text = self.convert_case(text, StringFormatter.CASE_UPPER)
        titlecase_text = self.convert_case(text, StringFormatter.CASE_TITLE)
        return lowercase_text, uppercase_text, titlecase_text

if __name__ == '__main__':
    sample_string = "A Different Sample String for Testing"
    formatter = StringFormatter()
    lower, upper, title = formatter.format_string(sample_string)
    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower}")
    print(f"Uppercase: {upper}")
    print(f"Title Case: {title}")