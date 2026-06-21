class NameSeparator:
    DELIMITER = '\t'

    @staticmethod
    def split_names(input_string):
        return [name.strip() for name in input_string.split(NameSeparator.DELIMITER) if name.strip()]

if __name__ == '__main__':
    separator = NameSeparator()
    sample_text = "Alice\tBob\tCharlie\tDavid"
    processed_data = separator.split_names(sample_text)
    print(processed_data)