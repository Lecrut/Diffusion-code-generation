class SpaceRemover:
    WHITESPACE_TYPES = (" ", "\t", "\n")

    @staticmethod
    def remove_spaces(input_string):
        for whitespace in SpaceRemover.WHITESPACE_TYPES:
            input_string = input_string.replace(whitespace, "")
        return input_string

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains spaces, tabs,\tand newlines."
    result = SpaceRemover.remove_spaces(sample_input)
    print(result)