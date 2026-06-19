class StringTransformer:
    def capitalize(self, text: str, rule: str) -> str:
        if rule == 'title':
            return self._to_title(text)
        elif rule == 'upper':
            return self._to_upper(text)
        elif rule == 'lower':
            return self._to_lower(text)
        else:
            raise ValueError("Unsupported capitalization rule")

    def _to_lower(self, text: str) -> str:
        return text.lower()

    def _to_upper(self, text: str) -> str:
        return text.upper()

    def _to_title(self, text: str) -> str:
        return text.title()

if __name__ == '__main__':
    transformer = StringTransformer()
    sample_string = "HeLlO wOrLd ThIs Is A TeSt"
    title_case = transformer.capitalize(sample_string, 'title')
    upper_case = transformer.capitalize(sample_string, 'upper')
    lower_case = transformer.capitalize(sample_string, 'lower')
    print(f"Original: {sample_string}")
    print(f"Title Case: {title_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Lowercase: {lower_case}")