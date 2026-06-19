class StringCapitalizer:
    def capitalize(self, text: str, rule: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        if not isinstance(rule, str):
            raise TypeError("Rule must be a string")
        
        rules = {
            'title': lambda t: t.title(),
            'upper': lambda t: t.upper(),
            'lower': lambda t: t.lower()
        }
        
        if rule in rules:
            return rules[rule](text)
        else:
            raise ValueError("Unsupported capitalization rule")

if __name__ == '__main__':
    capitalizer = StringCapitalizer()
    sample_string = "hello world"
    rule = 'title'
    try:
        capitalized_string = capitalizer.capitalize(sample_string, rule)
        print(capitalized_string)
    except (TypeError, ValueError) as e:
        print(e)