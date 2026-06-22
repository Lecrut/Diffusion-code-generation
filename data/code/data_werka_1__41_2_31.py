class StringCaseManipulator:
    LOWERCASE = 'lower'
    UPPERCASE = 'upper'
    TITLECASE = 'title'

    def transform(self, text, case_type):
        if case_type == self.LOWERCASE:
            return self._to_lower(text)
        elif case_type == self.UPPERCASE:
            return self._to_upper(text)
        elif case_type == self.TITLECASE:
            return self._to_title(text)
        else:
            raise ValueError("Invalid case type")

    def _to_lower(self, text):
        return text.lower()

    def _to_upper(self, text):
        return text.upper()

    def _to_title(self, text):
        return text.title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_string = "Hello World This Is A Test"
    print("Original:", sample_string)
    print("Lowercase:", manipulator.transform(sample_string, StringCaseManipulator.LOWERCASE))
    print("Uppercase:", manipulator.transform(sample_string, StringCaseManipulator.UPPERCASE))
    print("Title Case:", manipulator.transform(sample_string, StringCaseManipulator.TITLECASE))