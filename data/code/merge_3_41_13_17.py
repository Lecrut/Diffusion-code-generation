def apply_rule(text, rule_char):
        if not isinstance(rule_char, str) or len(rule_char) != 1:
            raise ValueError("Rule must be a single character string.")
        
        r = rule_char.lower()
        if r == 't': # Title case first letter only as per example logic
            return text[0].upper() + text[1:] if text and len(text) > 1 else text.upper()

if __name__ == '__main__':
    pass
