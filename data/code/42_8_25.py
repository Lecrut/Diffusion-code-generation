class StringJoiner:
    def __init__(self, separator):
        self.separator = separator

    def join_parts(self, parts):
        return self.separator.join(parts)

if __name__ == '__main__':
    SEPARATOR_NO_SPACE = ""
    SEPARATOR_WITH_SPACE = " "
    SEPARATOR_COMMA = ","

    string_joiner_no_space = StringJoiner(SEPARATOR_NO_SPACE)
    string_joiner_with_space = StringJoiner(SEPARATOR_WITH_SPACE)
    string_joiner_comma = StringJoiner(SEPARATOR_COMMA)

    parts = ["Hello", "world", "from", "Alibaba", "Cloud"]

    result_no_space = string_joiner_no_space.join_parts(parts)
    result_with_space = string_joiner_with_space.join_parts(parts)
    result_comma = string_joiner_comma.join_parts(parts)

    print(result_no_space)
    print(result_with_space)
    print(result_comma)