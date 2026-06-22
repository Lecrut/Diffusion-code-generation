class StringJoiner:
    NO_SEPARATOR = ""
    SPACE_SEPARATOR = " "
    COMMA_SEPARATOR = ","

    @staticmethod
    def join_strings(parts, separator=NO_SEPARATOR):
        return separator.join(parts)

if __name__ == '__main__':
    parts = ["Hello", "world", "This", "is", "a", "test"]
    result_no_separator = StringJoiner.join_strings(parts, StringJoiner.NO_SEPARATOR)
    result_space_separator = StringJoiner.join_strings(parts, StringJoiner.SPACE_SEPARATOR)
    result_comma_separator = StringJoiner.join_strings(parts, StringJoiner.COMMA_SEPARATOR)

    print("No separator:", result_no_separator)
    print("Space separator:", result_space_separator)
    print("Comma separator:", result_comma_separator)