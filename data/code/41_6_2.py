class StringCaseManipulator:
    @staticmethod
    def manipulate_case(input_string, case_type):
        if case_type == 'lower':
            return input_string.lower()
        elif case_type == 'upper':
            return input_string.upper()
        elif case_type == 'title':
            return input_string.title()
        else:
            return input_string
if __name__ == '__main__':
    sample_string = "Hello World Example"
    lower_case = StringCaseManipulator.manipulate_case(sample_string, 'lower')
    upper_case = StringCaseManipulator.manipulate_case(sample_string, 'upper')
    title_case = StringCaseManipulator.manipulate_case(sample_string, 'title')
    print(f"Original: {sample_string}")
    print(f"Lower: {lower_case}")
    print(f"Upper: {upper_case}")
    print(f"Title: {title_case}")