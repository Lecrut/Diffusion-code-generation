class SpaceConverter:
    SEPARATOR = '_'

    @staticmethod
    def _process_text(source):
        return source.replace(' ', SpaceConverter.SEPARATOR)

if __name__ == '__main__':
    original_string = "convert this space delimited string"
    converter = SpaceConverter()
    transformed = converter._process_text(original_string)
    print(transformed)