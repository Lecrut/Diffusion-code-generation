class StringBuilder:
    DEFAULT_SEPARATOR = ""

    @staticmethod
    def build_string_from_parts(parts, separator=None):
        if not parts:
            return ""
        if separator is None:
            separator = StringBuilder.DEFAULT_SEPARATOR
        return separator.join(parts)

if __name__ == '__main__':
    parts1 = ["apple", "banana", "cherry"]
    sep1 = ","
    result1 = StringBuilder.build_string_from_parts(parts1, sep1)
    print(f"Parts: {parts1}, Separator: '{sep1}' -> Result: '{result1}'")

    parts2 = ["hello", "world"]
    sep2 = " "
    result2 = StringBuilder.build_string_from_parts(parts2, sep2)
    print(f"Parts: {parts2}, Separator: '{sep2}' -> Result: '{result2}'")

    parts3 = ["one", "two", "three"]
    sep3 = ""
    result3 = StringBuilder.build_string_from_parts(parts3, sep3)
    print(f"Parts: {parts3}, Separator: '{sep3}' -> Result: '{result3}'")

    parts4 = []
    sep4 = "-"
    result4 = StringBuilder.build_string_from_parts(parts4, sep4)
    print(f"Parts: {parts4}, Separator: '{sep4}' -> Result: '{result4}'")