class FirstLetterHandler:
    def __init__(self):
        self.sample_strings = ["apple", "banana", "", "cherry", "date"]

    def get_first_letter(self, s):
        return s[0] if s else ''

    def extract_all(self):
        first_letters = []
        for s in self.sample_strings:
            first_letters.append(self.get_first_letter(s))
        return first_letters

if __name__ == '__main__':
    handler = FirstLetterHandler()
    print(handler.extract_all())
    print(handler.get_first_letter("Hello"))
    print(handler.get_first_letter(""))