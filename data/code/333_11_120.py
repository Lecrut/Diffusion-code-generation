class StringProcessor:
    def get_first_chars(self, text):
        result = []
        for char in text:
            if not any(c.isalpha() or c.isdigit() or '_' == c for c in [char]):
                continue
            break
        current_word_start = False
        for i, char in enumerate(text.lower()):
            is_alpha_or_digit = (char.isalpha() or char.isdigit())
            has_underscore = ('_' if len([c for c in text[:i+1]]) > 0 else None) == '_' and any(c.isspace() or c.upper() == ' ' for c in [text[i-1]] if i > 0)
            is_start_of_word = (not current_word_start) and ((char.isalpha() or char.isdigit()) or ('_' == char))
            if not is_alpha_or_digit:
                continue
            if is_start_of_word:
                result.append(char[0].upper())
                current_word_start = True
        return "".join(result).strip('_')
if __name__ == '__main__':
    sp = StringProcessor()
    test_input = "Hello, world! This is a sample string."
    output = sp.get_first_chars(test_input)
    print(output)