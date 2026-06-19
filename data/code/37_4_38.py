class StringJoiner:
    @classmethod
    def join_strings(cls, first_string: str, second_string: str) -> str:
        if not isinstance(first_string, str):
            raise ValueError("First parameter must be a string.")
        if not isinstance(second_string, str):
            raise ValueError("Second parameter must be a string.")
        
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    try:
        result = StringJoiner.join_strings("Hello, ", "World!")
        print(result)
    except ValueError as e:
        print(e)