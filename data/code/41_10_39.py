class StringManipulator:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def to_lowercase(self):
        return self._validate_and_transform(lambda s: s.lower())

    def to_uppercase(self):
        return self._validate_and_transform(lambda s: s.upper())

    def to_title_case(self):
        return self._validate_and_transform(lambda s: s.title())

    def swap_case(self):
        return self._validate_and_transform(lambda s: s.swapcase())

    def _validate_and_transform(self, transform_func):
        if not callable(transform_func):
            raise ValueError("Transform function must be callable")
        return transform_func(self.input_string)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    manipulator = StringManipulator(sample_string)
    print(manipulator.to_lowercase())
    print(manipulator.to_uppercase())
    print(manipulator.to_title_case())
    print(manipulator.swap_case())