class StringFormatter:
    @staticmethod
    def to_lowercase(text):
        return text.lower()

    @staticmethod
    def to_uppercase(text):
        return text.upper()

    @staticmethod
    def to_titlecase(text):
        return text.title()

if __name__ == '__main__':
    sample_string = "Transform This String"
    lower = StringFormatter.to_lowercase(sample_string)
    upper = StringFormatter.to_uppercase(sample_string)
    title = StringFormatter.to_titlecase(sample_string)
    
    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower}")
    print(f"Uppercase: {upper}")
    print(f"Title Case: {title}")