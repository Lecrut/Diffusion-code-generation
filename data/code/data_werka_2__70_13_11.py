class StringAccessor:
    _FIRST_OFFSET = 0
    _LAST_OFFSET = -1

    @staticmethod
    def extract_chars(text: str) -> tuple:
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        if len(text) == 0:
            raise ValueError("Input must not be empty")
        first_idx = StringAccessor._FIRST_OFFSET
        last_idx = StringAccessor._LAST_OFFSET
        return (text[first_idx], text[last_idx])

if __name__ == '__main__':
    sample_text = "Python"
    result = StringAccessor.extract_chars(sample_text)
    print(result)