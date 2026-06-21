import unicodedata
import re

class PasswordPolicyEnforcer:
    MAX_UNICODE_CODEPOINT = 0x10FFFF
    SURROGATE_START = 0xD800
    SURROGATE_END = 0xDFFF
    MIN_CLASSES = 3

    def __init__(self, password_string):
        self.raw_input = password_string
        self.is_unicode_compliant = self._verify_unicode_safety()
        self.classes_found = self._identify_present_classes()

    def _verify_unicode_safety(self):
        if not isinstance(self.raw_input, str):
            return False
        try:
            self.raw_input.encode('utf-32')
        except UnicodeError:
            return False
        for character in self.raw_input:
            code_val = ord(character)
            if code_val > self.MAX_UNICODE_CODEPOINT:
                return False
            if self.SURROGATE_START <= code_val <= self.SURROGATE_END:
                return False
        return True

    def _identify_present_classes(self):
        if not self.is_unicode_compliant:
            return set()
        detected_classes = set()
        for character in self.raw_input:
            category = unicodedata.category(character)
            if category.startswith('Lu'):
                detected_classes.add('upper')
            elif category.startswith('Ll'):
                detected_classes.add('lower')
            elif category.startswith('Nd'):
                detected_classes.add('digit')
            else:
                if not character.isalnum():
                    detected_classes.add('special')
        return detected_classes

    def is_valid(self):
        if not self.is_unicode_compliant:
            return False
        return len(self.classes_found) >= self.MIN_CLASSES

    def get_details(self):
        return {
            "unicode_ok": self.is_unicode_compliant,
            "classes": sorted(list(self.classes_found)),
            "count": len(self.classes_found),
            "valid": self.is_valid()
        }

def check_password_strength(candidate):
    enforcer = PasswordPolicyEnforcer(candidate)
    return enforcer.get_details()

if __name__ == '__main__':
    test_cases = [
        "Secure123!",
        "alllowercase",
        "ABC123",
        "Special@#%",
        "Mix3dW1thSymb0ls",
        "12345678",
        "UPPERCASEONLY",
        "NoDigitsHere!",
        "JustLetters",
        "!@#$%^&*()"
    ]

    for pwd in test_cases:
        result = check_password_strength(pwd)
        print(f"Password: '{pwd}' -> {result}")