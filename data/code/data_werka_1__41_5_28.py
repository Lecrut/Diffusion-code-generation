class CaseManipulator:
    LOWER = 1
    UPPER = 2
    TITLE = 3

    def __init__(self, text):
        self.text = text

    def convert_case(self, case_type):
        if case_type == self.LOWER:
            return self._to_lower()
        elif case_type == self.UPPER:
            return self._to_upper()
        elif case_type == self.TITLE:
            return self._to_title()
        else:
            raise ValueError("Invalid case type")

    def _to_lower(self):
        return self.text.lower()

    def _to_upper(self):
        return self.text.upper()

    def _to_title(self):
        return self.text.title()

if __name__ == '__main__':
    sample_string = "HeLlO WoRlD"
    manipulator = CaseManipulator(sample_string)
    
    print("Original:", sample_string)
    print("Lowercase:", manipulator.convert_case(CaseManipulator.LOWER))
    print("Uppercase:", manipulator.convert_case(CaseManipulator.UPPER))
    print("Titlecase:", manipulator.convert_case(CaseManipulator.TITLE))