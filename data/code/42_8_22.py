class StringJoiner:
    def __init__(self, separator=""):
        self.separator = separator

    def join(self, parts):
        if not isinstance(parts, list) or not all(isinstance(part, str) for part in parts):
            raise ValueError("Parts must be a list of strings.")
        return self.separator.join(parts)

if __name__ == '__main__':
    try:
        string_joiner = StringJoiner(separator=" ")
        parts = ["Hello", "world", "This", "is", "a", "test."]
        result = string_joiner.join(parts)
        print(result)
    except ValueError as e:
        print(e)