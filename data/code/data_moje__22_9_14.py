import unicodedata
import string

class PasswordValidator:
    VALID_UNICODE_MAX = 0x10FFFF
    SURROGATE_LOW = 0xD800
    SURROGATE_HIGH = 0xDFFF
    
    def __init__(self, password):
        self.password = password

    def _is_unicode_valid(self):
        for char in self.password:
            code = ord(char)
            if code > self.VALID_UNICODE_MAX:
                return False
            if self.SURROGATE_LOW <= code <= self.SURROGATE_HIGH:
                return False
        return True

    def _count_categories(self):
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False
        
        for char in self.password:
            category = unicodedata.category(char)
            
            if category.startswith('Lu'):
                has_upper = True
            elif category.startswith('Ll') or category.startswith('Lt') or category.startswith('Lm') or category.startswith('Lo'):
                has_lower = True
            elif category.startswith('Nd'):
                has_digit = True
            else:
                has_symbol = True
                
        count = sum([has_upper, has_lower, has_digit, has_symbol])
        return count

    def validate(self):
        if not self._is_unicode_valid():
            return False
        return self._count_categories() >= 3

if __name__ == '__main__':
    validator1 = PasswordValidator("Hello123!World")
    print(validator1.validate())
    
    validator2 = PasswordValidator("abc")
    print(validator2.validate())
    
    validator3 = PasswordValidator("A1!")
    print(validator3.validate())
    
    validator4 = PasswordValidator("Test_42")
    print(validator4.validate())
    
    validator5 = PasswordValidator("\ud800")
    print(validator5.validate())