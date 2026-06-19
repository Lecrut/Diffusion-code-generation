class StringCapitalizer:
    def capitalize(self, text: str, rule: str) -> str:
        if rule == 'title':
            return self._to_title(text)
        elif rule == 'upper':
            return self._to_upper(text)
        elif rule == 'lower':
            return self._to_lower(text)
        else:
            raise ValueError("Unsupported capitalization rule")

    def _to_title(self, text: str) -> str:
        return text.title()

    def _to_upper(self, text: str) -> str:
        return text.upper()

    def _to_lower(self, text: str) -> str:
        return text.lower()

if __name__ == '__main__':
    capitalizer = StringCapitalizer()
    sample_string = "greetings from alibaba cloud"
    rule = 'title'
    capitalized_string = capitalizer.capitalize(sample_string, rule)
    print(capitalized_string)