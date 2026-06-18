class StringAppender:
    @staticmethod
    def append_strings(first_string: str, second_string: str) -> str:
        """Returns a new string formed by appending the second argument to the first."""
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    result = StringAppender.append_strings("Hello", "World")
    print(result)