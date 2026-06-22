class StringListProcessor:
    MINIMUM_LENGTH = 2

    @staticmethod
    def validate_list_length(strings):
        if len(strings) < StringListProcessor.MINIMUM_LENGTH:
            raise ValueError("The list must contain at least two elements.")
    
    @staticmethod
    def get_second_string(strings):
        StringListProcessor.validate_list_length(strings)
        return strings[1]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    try:
        second_string = StringListProcessor.get_second_string(sample_strings)
        print(second_string)
    except ValueError as e:
        print(e)