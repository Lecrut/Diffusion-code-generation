from collections import Counter

CHAR_LIMIT = 128

def is_unique(input_str: str) -> bool:
    if len(input_str) > CHAR_LIMIT:
        return False
    frequency_map = Counter(input_str)
    for count in frequency_map.values():
        if count > 1:
            return False
    return True

class StringValidator:
    def __init__(self, text: str):
        self.text = text
    
    def check_uniqueness(self) -> bool:
        return is_unique(self.text)

if __name__ == '__main__':
    test_string = "python"
    validator_instance = StringValidator(test_string)
    print(validator_instance.check_uniqueness())
    print(is_unique("programming"))