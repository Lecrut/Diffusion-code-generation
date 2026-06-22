class AlphaExtractor:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_first_alpha(self):
        for char in self.input_string:
            if char.isalpha():
                return char
        return ""

if __name__ == '__main__':
    extractor1 = AlphaExtractor("Hello")
    print(extractor1.get_first_alpha())

    extractor2 = AlphaExtractor("")
    print(extractor2.get_first_alpha())

    extractor3 = AlphaExtractor("a")
    print(extractor3.get_first_alpha())

    extractor4 = AlphaExtractor("Python")
    print(extractor4.get_first_alpha())

    extractor5 = AlphaExtractor("!@#abc")
    print(extractor5.get_first_alpha())

    extractor6 = AlphaExtractor("123456")
    print(extractor6.get_first_alpha())

    extractor7 = AlphaExtractor("no leading numbers")
    print(extractor7.get_first_alpha())

    extractor8 = AlphaExtractor(" ")
    print(extractor8.get_first_alpha())