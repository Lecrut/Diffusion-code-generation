class StringConcatenator:
    def __init__(self, input_list):
        if not all(isinstance(s, str) for s in input_list):
            raise TypeError("All elements must be strings")
        self.input_list = input_list

    def concatenate(self, separator=""):
        return separator.join(self.input_list)

if __name__ == '__main__':
    sample_values = ["Hello", " ", "World", "!"]
    try:
        concat_obj = StringConcatenator(sample_values)
        result_with_space = concat_obj.concatenate(" ")
        result_without_separator = concat_obj.concatenate()
        print(result_with_space)
        print(result_without_separator)
    except TypeError as e:
        print(e)