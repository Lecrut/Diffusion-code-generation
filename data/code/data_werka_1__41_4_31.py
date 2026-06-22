class CaseConverter:
    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    TITLECASE = 'titlecase'

    @staticmethod
    def convert_char(char, case):
        if case == CaseConverter.LOWERCASE:
            return char.lower()
        elif case == CaseConverter.UPPERCASE:
            return char.upper()
        elif case == CaseConverter.TITLECASE:
            return char.upper() if not char.isalnum() else char.lower()

    @staticmethod
    def convert_string(s, case):
        result = []
        for i, char in enumerate(s):
            if i == 0 and case == CaseConverter.TITLECASE:
                result.append(char.upper())
            else:
                result.append(CaseConverter.convert_char(char, case))
        return ''.join(result)

    @staticmethod
    def case_converter(s):
        lower_case = CaseConverter.convert_string(s, CaseConverter.LOWERCASE)
        upper_case = CaseConverter.convert_string(s, CaseConverter.UPPERCASE)
        title_case = CaseConverter.convert_string(s, CaseConverter.TITLECASE)
        return lower_case, upper_case, title_case

if __name__ == '__main__':
    sample_string = "this is a sample string for testing"
    lower, upper, title = CaseConverter.case_converter(sample_string)
    print(lower)
    print(upper)
    print(title)