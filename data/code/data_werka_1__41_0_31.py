class StringFormatter:
    def __init__(self, text):
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def to_uppercase(self):
        return self.text.upper()

    def to_title_case(self):
        return self.text.title()

if __name__ == '__main__':
    sample_string = "Convert This String To Different Cases"
    formatter = StringFormatter(sample_string)
    print(formatter.to_lowercase())
    print(formatter.to_uppercase())
    print(formatter.to_title_case())