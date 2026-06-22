class StringFormatter:
    def __init__(self, text):
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def to_uppercase(self):
        return self.text.upper()

    def to_titlecase(self):
        return self.text.title()

if __name__ == '__main__':
    sample_string = "This is a Test String for Formatting."
    formatter = StringFormatter(sample_string)
    
    print(formatter.to_lowercase())
    print(formatter.to_uppercase())
    print(formatter.to_titlecase())