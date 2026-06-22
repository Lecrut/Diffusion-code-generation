class StringCapitalizer:
    def capitalize(self, text: str, rule: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        if not isinstance(rule, str):
            raise TypeError("Rule must be a string")

        if rule == 'title':
            return text.title()
        elif rule == 'upper':
            return text.upper()
        elif rule == 'lower':
            return text.lower()
        else:
            raise ValueError("Unsupported capitalization rule")

if __name__ == '__main__':
    capitalizer = StringCapitalizer()
    sample_string = "hello world"
    rule = 'title'
    capitalized_string = capitalizer.capitalize(sample_string, rule)
    print(capitalized_string)