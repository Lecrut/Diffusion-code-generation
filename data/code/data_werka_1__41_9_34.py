class CaseManipulator:
    CASE_LOWER = 'lower'
    CASE_UPPER = 'upper'
    CASE_TITLE = 'title'
    CASE_SWAP = 'swap'

    @staticmethod
    def _validate_case(case):
        valid_cases = {CaseManipulator.CASE_LOWER, CaseManipulator.CASE_UPPER, 
                      CaseManipulator.CASE_TITLE, CaseManipulator.CASE_SWAP}
        if case not in valid_cases:
            raise ValueError(f'Invalid case specified: {case}. Valid cases are: {valid_cases}')

    @staticmethod
    def manipulate_case(text, case=CASE_LOWER):
        CaseManipulator._validate_case(case)
        methods = {
            CaseManipulator.CASE_LOWER: str.lower,
            CaseManipulator.CASE_UPPER: str.upper,
            CaseManipulator.CASE_TITLE: str.title,
            CaseManipulator.CASE_SWAP: str.swapcase
        }
        return methods[case](text)

if __name__ == '__main__':
    sample_text = "Hello World Example"
    print(CaseManipulator.manipulate_case(sample_text, CaseManipulator.CASE_LOWER))
    print(CaseManipulator.manipulate_case(sample_text, CaseManipulator.CASE_UPPER))
    print(CaseManipulator.manipulate_case(sample_text, CaseManipulator.CASE_TITLE))
    print(CaseManipulator.manipulate_case(sample_text, CaseManipulator.CASE_SWAP))