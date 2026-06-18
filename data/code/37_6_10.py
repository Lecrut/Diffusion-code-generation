class StringAppender:
    def append(self, first_string: str, second_string: str) -> str:
        """Returns a new string formed by appending the second string to the first."""
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    appender = StringAppender()
    result = appender.append("Hello", "World!")
    print(result)