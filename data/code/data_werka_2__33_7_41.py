class SpaceRemover:
    WHITESPACE_CHARS = (' ', '\t', '\n', '\r')

    @staticmethod
    def remove_all_spaces(input_string):
        result = []
        for char in input_string:
            if char not in SpaceRemover.WHITESPACE_CHARS:
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various whitespace characters."
    remover = SpaceRemover()
    result = remover.remove_all_spaces(sample_input)
    print(result)