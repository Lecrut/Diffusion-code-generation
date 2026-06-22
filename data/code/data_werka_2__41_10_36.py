class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def to_lowercase(self):
        return self.input_string.lower()

    def to_uppercase(self):
        return self.input_string.upper()

    def to_title_case(self):
        return self.input_string.title()

    def swap_case(self):
        return self.input_string.swapcase()

if __name__ == '__main__':
    sample_values = {
        "original": "Hello, World!",
        "lowercase": None,
        "uppercase": None,
        "title_case": None,
        "swap_case": None
    }

    manipulator = StringManipulator(sample_values["original"])
    sample_values["lowercase"] = manipulator.to_lowercase()
    sample_values["uppercase"] = manipulator.to_uppercase()
    sample_values["title_case"] = manipulator.to_title_case()
    sample_values["swap_case"] = manipulator.swap_case()

    for key, value in sample_values.items():
        print(f"{key}: {value}")