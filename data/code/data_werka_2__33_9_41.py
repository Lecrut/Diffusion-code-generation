class TextMinifier:
    WHITESPACE_CHARS = {' ', '\t', '\n', '\r'}

    @staticmethod
    def _is_whitespace(char):
        return char in TextMinifier.WHITESPACE_CHARS

    @staticmethod
    def minify_text(input_string):
        if not isinstance(input_string, str):
            raise ValueError('Input must be a string')
        
        result = []
        last_was_whitespace = False
        
        for char in input_string:
            if TextMinifier._is_whitespace(char):
                if not last_was_whitespace:
                    result.append(' ')
                    last_was_whitespace = True
            else:
                result.append(char)
                last_was_whitespace = False
        
        return ''.join(result).strip()

if __name__ == '__main__':
    sample_input = "   This is a\ttest string.\nIt contains various whitespaces.  "
    result = TextMinifier.minify_text(sample_input)
    print(result)