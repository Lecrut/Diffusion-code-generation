class StringCaseConverter:
    @staticmethod
    def to_lowercase_and_swap_case(text: str) -> str:
        return text.lower().swapcase()

if __name__ == '__main__':
    sample_string = 'Hello World'
    result = StringCaseConverter.to_lowercase_and_swap_case(sample_string)
    print(result)