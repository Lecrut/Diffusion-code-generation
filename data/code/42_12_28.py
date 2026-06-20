class StringBuilder:
    def __init__(self):
        self._internal_string = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        joined_part = separator.join(parts)
        if self._internal_string and joined_part:
            self._internal_string += separator + joined_part
        elif joined_part:
            self._internal_string += joined_part
        return self._internal_string

if __name__ == '__main__':
    builder = StringBuilder()
    result1 = builder.append_and_join(["a", "b", "c"], "-")
    print(result1)
    result2 = builder.append_and_join(["x", "y"], "|")
    print(result2)