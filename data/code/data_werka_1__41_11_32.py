class TextFormatter:
    def __init__(self, text: str):
        self.text = text

    def capitalize(self, rule: str) -> str:
        if rule == 'title':
            return self.text.title()
        elif rule == 'upper':
            return self.text.upper()
        elif rule == 'lower':
            return self.text.lower()
        else:
            raise ValueError("Unsupported capitalization rule")

if __name__ == '__main__':
    sample_text = "hello world"
    formatter = TextFormatter(sample_text)
    title_case = formatter.capitalize('title')
    upper_case = formatter.capitalize('upper')
    lower_case = formatter.capitalize('lower')
    print(f"Original: {sample_text}")
    print(f"Title Case: {title_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Lowercase: {lower_case}")