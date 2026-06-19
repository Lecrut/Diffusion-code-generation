class CaseConverter:
    def __init__(self, s):
        self.original = s
        self.lower_case = ""
        self.upper_case = ""
        self.title_case = ""
        self._convert_cases()

    def _convert_cases(self):
        for char in self.original:
            if 'a' <= char <= 'z':
                self.lower_case += char
                self.upper_case += chr(ord(char) - 32)
                self.title_case += (chr(ord(char) - 32) if not self.title_case else char)
            elif 'A' <= char <= 'Z':
                self.lower_case += chr(ord(char) + 32)
                self.upper_case += char
                self.title_case += char if not self.title_case else chr(ord(char) + 32)
            else:
                self.lower_case += char
                self.upper_case += char
                self.title_case += char

    def get_lower_case(self):
        return self.lower_case

    def get_upper_case(self):
        return self.upper_case

    def get_title_case(self):
        return self.title_case

if __name__ == '__main__':
    sample_string = "this is a sample string for testing"
    converter = CaseConverter(sample_string)
    print(converter.get_lower_case())
    print(converter.get_upper_case())
    print(converter.get_title_case())