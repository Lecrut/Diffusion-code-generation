class CaseManipulator:
    CASE_LOWER = 'lower'
    CASE_UPPER = 'upper'
    CASE_TITLE = 'title'

    def __init__(self, text):
        self.text = text

    @staticmethod
    def _convert(text, case_type):
        if case_type == CaseManipulator.CASE_LOWER:
            return text.lower()
        elif case_type == CaseManipulator.CASE_UPPER:
            return text.upper()
        elif case_type == CaseManipulator.CASE_TITLE:
            return text.title()
        else:
            raise ValueError("Invalid case type")

    def convert(self, case_type):
        return self._convert(self.text, case_type)

if __name__ == '__main__':
    sample_string = "HeLlO WoRlD"
    manipulator = CaseManipulator(sample_string)
    print(manipulator.convert(CaseManipulator.CASE_LOWER))
    print(manipulator.convert(CaseManipulator.CASE_UPPER))
    print(manipulator.convert(CaseManipulator.CASE_TITLE))