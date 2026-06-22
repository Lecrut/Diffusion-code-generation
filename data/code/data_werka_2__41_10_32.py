class StringManipulator:
    def __init__(self, input_str):
        self.input_str = input_str

    def to_lowercase(self):
        return self.input_str.lower()

    def to_uppercase(self):
        return self.input_str.upper()

    def to_title_case(self):
        return self.input_str.title()

    def swap_case(self):
        return self.input_str.swapcase()

if __name__ == '__main__':
    sample_input = "The Quick Brown Fox"
    manipulator_instance = StringManipulator(sample_input)
    
    lowercased_result = manipulator_instance.to_lowercase()
    uppercased_result = manipulator_instance.to_uppercase()
    titlecased_result = manipulator_instance.to_title_case()
    swapped_case_result = manipulator_instance.swap_case()

    print("Original:", sample_input)
    print("Lowercased:", lowercased_result)
    print("Uppercased:", uppercased_result)
    print("Titlecased:", titlecased_result)
    print("Swapped Case:", swapped_case_result)