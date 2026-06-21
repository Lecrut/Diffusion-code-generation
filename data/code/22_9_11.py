import unicodedata

class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def is_unicode_valid(self):
        for char in self.password:
            cp = ord(char)
            if cp > 0x10FFFF:
                return False
            if 0xD800 <= cp <= 0xDFFF:
                return False
        return True

    def validate(self):
        if not self.is_unicode_valid():
            return False
        
        has_upper = any(char.isupper() for char in self.password)
        has_lower = any(char.islower() for char in self.password)
        has_digit = any(char.isdigit() for char in self.password)
        
        has_symbol = False
        for char in self.password:
            if not char.isalnum() and not char.isspace():
                has_symbol = True
                break
        
        classes_present = 0
        if has_upper:
            classes_present += 1
        if has_lower:
            classes_present += 1
        if has_digit:
            classes_present += 1
        if has_symbol:
            classes_present += 1
            
        return classes_present >= 3

if __name__ == '__main__':
    validator1 = PasswordValidator("Hello123!")
    print(validator1.validate())
    
    validator2 = PasswordValidator("hello123")
    print(validator2.validate())
    
    validator3 = PasswordValidator("HELLO!@#")
    print(validator3.validate())
    
    validator4 = PasswordValidator("")
    print(validator4.validate())
    
    validator5 = PasswordValidator("Abc")
    print(validator5.validate())