class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def first_alphabetic_character(self):
        for char in self.input_string:
            if char.isalpha():
                return char
        return None

if __name__ == '__main__':
    processor1 = StringProcessor("123abc456")
    print(processor1.first_alphabetic_character())

    processor2 = StringProcessor("!!!hello")
    print(processor2.first_alphabetic_character())

    processor3 = StringProcessor("9876xyz")
    print(processor3.first_alphabetic_character())

    processor4 = StringProcessor("   ")
    print(processor4.first_alphabetic_character())

    processor5 = StringProcessor("")
    print(processor5.first_alphabetic_character())