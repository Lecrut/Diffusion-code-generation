class StringFormatter:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def to_uppercase(self):
        return self.text.upper()

    def to_titlecase(self):
        return self.text.title()

if __name__ == '__main__':
    sample_string = "Hello World, This is a Test String."
    formatter = StringFormatter(sample_string)
    
    print(formatter.to_lowercase())
    print(formatter.to_uppercase())
    print(formatter.to_titlecase())