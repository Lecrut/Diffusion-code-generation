class StringCaseManipulator:
    def to_lowercase(self, s):
        return s.lower()

    def to_uppercase(self, s):
        return s.upper()

    def to_title_case(self, s):
        return s.title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_string = 'Hello, World!'
    print("Original:", sample_string)
    print("Lowercase:", manipulator.to_lowercase(sample_string))
    print("Uppercase:", manipulator.to_uppercase(sample_string))
    print("Title Case:", manipulator.to_title_case(sample_string))