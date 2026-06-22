class StringManipulator:
    CASE_LOWER = "lowercase"
    CASE_UPPER = "uppercase"
    CASE_TITLE = "title_case"

    @staticmethod
    def manipulate_case(input_string):
        return {
            StringManipulator.CASE_LOWER: input_string.lower(),
            StringManipulator.CASE_UPPER: input_string.upper(),
            StringManipulator.CASE_TITLE: input_string.title()
        }

if __name__ == '__main__':
    sample_input = "Sample Input String"
    result = StringManipulator.manipulate_case(sample_input)
    print(result)