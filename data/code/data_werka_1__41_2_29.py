class StringCaseManipulator:
    def transform(self, text):
        return self._validate_text(text)

    def to_lower(self, text):
        return self._to_lower(self._validate_text(text))

    def to_upper(self, text):
        return self._to_upper(self._validate_text(text))

    def to_title(self, text):
        return self._to_title(self._validate_text(text))

    def _validate_text(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text

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
    print("Lowercase:", manipulator.to_lower(sample_string))
    print("Uppercase:", manipulator.to_upper(sample_string))
    print("Title Case:", manipulator.to_title(sample_string))