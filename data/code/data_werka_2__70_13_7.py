class _StringAccessor:
    FIRST_IDX: int = 0
    LAST_IDX: int = -1

    @staticmethod
    def _validate(input_str: str) -> str:
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")
        if len(input_str) == 0:
            raise ValueError("Input must not be empty")
        return input_str

    @staticmethod
    def get_bounds(input_str: str) -> tuple:
        validated = _StringAccessor._validate(input_str)
        return (validated[_StringAccessor.FIRST_IDX], validated[_StringAccessor.LAST_IDX])

if __name__ == '__main__':
    sample_text: str = "algorithm"
    result: tuple = _StringAccessor.get_bounds(sample_text)
    print(result)