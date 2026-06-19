class StringJoiner:
    @classmethod
    def join_strings(cls, first_string, second_string):
        if not isinstance(first_string, str) or not isinstance(second_string, str):
            raise ValueError("Both inputs must be strings")
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    try:
        result = StringJoiner.join_strings("Hello, ", "World!")
        print(result)
    except ValueError as e:
        print(e)