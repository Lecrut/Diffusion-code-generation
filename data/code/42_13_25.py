class StringConcatenator:
    DEFAULT_SEPARATOR = ", "

    @staticmethod
    def validate_input(input_list):
        if not all(isinstance(s, str) for s in input_list):
            raise TypeError("All elements must be strings")

    @classmethod
    def concatenate(cls, input_list, separator=DEFAULT_SEPARATOR):
        cls.validate_input(input_list)
        return separator.join(input_list)

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    try:
        result = StringConcatenator.concatenate(sample_values, "; ")
        print(result)
    except TypeError as e:
        print(e)