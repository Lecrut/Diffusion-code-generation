class StringFilter:
    ALPHANUMERIC_PATTERN = '[^a-zA-Z0-9]'
    
    @staticmethod
    def _filter_non_alphanumeric(input_string):
        return re.sub(StringFilter.ALPHANUMERIC_PATTERN, '', input_string)
    
    @classmethod
    def filter_alphanumeric(cls, input_string):
        return cls._filter_non_alphanumeric(input_string)

if __name__ == '__main__':
    sample_input = 'Hello, World! 123.'
    result = StringFilter.filter_alphanumeric(sample_input)
    print(result)