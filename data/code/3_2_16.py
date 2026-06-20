import re

PATTERN = r'[aeiouAEIOU]'

def _validate_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if len(text) == 0:
        return False
    return True

def remove_vowels(text):
    if not _validate_input(text):
        return text
    return re.sub(PATTERN, '', text)

class VowelFilter:
    def __init__(self, text):
        self.original = text
        self.filtered = None
    
    def process(self):
        if _validate_input(self.original):
            self.filtered = re.sub(PATTERN, '', self.original)
        else:
            self.filtered = self.original
        return self.filtered
    
    def get_result(self):
        return self.filtered

if __name__ == '__main__':
    sample1 = "Programming is Fun"
    sample2 = "AEIOU aeiou"
    sample3 = "BCDFG"
    
    func_result = remove_vowels(sample1)
    print(func_result)
    
    obj = VowelFilter(sample2)
    obj.process()
    print(obj.get_result())
    
    print(remove_vowels(sample3))