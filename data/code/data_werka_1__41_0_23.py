class StringFormatter:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def to_uppercase(self):
        return self.text.upper()

    def to_title_case(self):
        return self.text.title()

if __name__ == '__main__':
    sample_string = "Hello World, This is a Test String."
    formatter = StringFormatter(sample_string)
    
    try:
        lowercase_text = formatter.to_lowercase()
        uppercase_text = formatter.to_uppercase()
        titlecase_text = formatter.to_title_case()
        
        print(f"Original: {sample_string}")
        print(f"Lowercase: {lowercase_text}")
        print(f"Uppercase: {uppercase_text}")
        print(f"Title Case: {titlecase_text}")
    except ValueError as e:
        print(e)