import re

class VowelStripper:
    _VOWEL_PATTERN = re.compile(r'[aeiouAEIOU]')

    def __init__(self, input_text):
        self.input_text = input_text
        self.stripped_text = self._VOWEL_PATTERN.sub('', input_text)

    def get_result(self):
        return self.stripped_text

    def get_original(self):
        return self.input_text

    def process_text(self, new_text):
        self.input_text = new_text
        self.stripped_text = self._VOWEL_PATTERN.sub('', new_text)
        return self.stripped_text

if __name__ == '__main__':
    text_1 = "Beautiful Morning"
    stripper_1 = VowelStripper(text_1)
    print(stripper_1.get_result())
    print(stripper_1.get_original())
    print(stripper_1.process_text("Dynamic Code"))