class StringBuilder:
    SEPARATOR = " "

    @staticmethod
    def build_string_from_parts(parts):
        return StringBuilder.SEPARATOR.join(parts)

if __name__ == '__main__':
    sample_parts = ["hello", "world", "from", "python"]
    output = StringBuilder.build_string_from_parts(sample_parts)
    print(output)