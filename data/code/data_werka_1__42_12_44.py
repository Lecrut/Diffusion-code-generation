class StringBuilder:
    def __init__(self):
        self.content = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not isinstance(parts, list):
            raise TypeError("parts must be a list of strings")
        if not all(isinstance(part, str) for part in parts):
            raise ValueError("All elements in parts must be strings")
        if not isinstance(separator, str):
            raise TypeError("separator must be a string")

        self.content += separator.join(parts)
        return self.content

if __name__ == '__main__':
    builder = StringBuilder()
    sample_parts = ["Hello", "world", "this", "is", "a", "test"]
    separator = ", "
    try:
        result = builder.append_and_join(sample_parts, separator)
        print(result)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")