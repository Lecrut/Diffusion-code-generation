class NameUtils:
    SEPARATOR = '-'

    @staticmethod
    def trim_names(name_string):
        return [name.strip() for name in name_string.split(NameUtils.SEPARATOR)]

if __name__ == '__main__':
    sample_input = "  John-Doe - Jane-Smith  "
    print(NameUtils.trim_names(sample_input))