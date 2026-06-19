class StringManipulator:
    def capitalize(self, text: str, rule: str) -> str:
        if rule == 'title':
            return self.to_title(text)
        elif rule == 'upper':
            return self.to_upper(text)
        elif rule == 'lower':
            return self.to_lower(text)
        else:
            raise ValueError("Unsupported capitalization rule")

    def to_lower(self, text: str) -> str:
        return text.lower()

    def to_upper(self, text: str) -> str:
        return text.upper()

    def to_title(self, text: str) -> str:
        return text.title()

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_string = "hello world"
    
    title_case = manipulator.capitalize(sample_string, 'title')
    upper_case = manipulator.capitalize(sample_string, 'upper')
    lower_case = manipulator.capitalize(sample_string, 'lower')
    
    print(f"Original: {sample_string}")
    print(f"Title Case: {title_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Lowercase: {lower_case}")