class CaseManipulator:
    CASES = {
        'lower': str.lower,
        'upper': str.upper,
        'title': str.title,
        'swap': str.swapcase
    }

    @staticmethod
    def manipulate_case(text, case='lower'):
        if case not in CaseManipulator.CASES:
            raise ValueError(f"Invalid case specified: {case}. Valid cases are: {', '.join(CaseManipulator.CASES.keys())}")
        return CaseManipulator.CASES[case](text)

if __name__ == '__main__':
    sample_text = "Hello World Example"
    print(CaseManipulator.manipulate_case(sample_text, 'lower'))
    print(CaseManipulator.manipulate_case(sample_text, 'upper'))
    print(CaseManipulator.manipulate_case(sample_text, 'title'))
    print(CaseManipulator.manipulate_case(sample_text, 'swap'))