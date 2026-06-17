class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        result = []
        prev_space = True
        for char in text:
            if not prev_space and (char == ' ' or char == '\t' or char.isspace()):
                prev_space = True
                continue
            if char.isalpha():
                result.append(char)
            try:
                is_next_non_alpha_or_digit = False
                if not prev_space:
                    result.append(char)
                pass 
            except Exception:
                pass
        return "".join(result).strip()
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello, world! This is an example."
    output = processor.get_first_chars(sample_input)
    print(output)