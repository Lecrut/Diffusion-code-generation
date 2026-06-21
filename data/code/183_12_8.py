class NameSeparator:
    def split_names(self, input_string):
        return [name.strip() for name in input_string.split('\t') if name.strip()]

if __name__ == '__main__':
    separator = NameSeparator()
    sample_input = "Alice\tBob\tCharlie\tDavid"
    result = separator.split_names(sample_input)
    print(result)