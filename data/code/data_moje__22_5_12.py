class PasswordValidator:
    MIN_LENGTH = 8
    SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"

    def __init__(self, username, email):
        self.username = username.lower()
        self.domain = ""
        if "@" in email:
            self.domain = email.split("@")[-1].lower()
        else:
            self.domain = email.lower() if email else ""

    def check_username_or_domain(self, password):
        pwd_lower = password.lower()
        if self.username and self.username in pwd_lower:
            return False
        if self.domain and self.domain in pwd_lower:
            return False
        return True

    def check_complexity(self, password):
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in self.SPECIAL_CHARS:
                has_special = True
        
        return has_upper and has_lower and has_digit and has_special

    def validate(self, password):
        if not password or len(password) < self.MIN_LENGTH:
            return False
        if not self.check_username_or_domain(password):
            return False
        if not self.check_complexity(password):
            return False
        return True

if __name__ == '__main__':
    validator = PasswordValidator("alice_smith", "alice.smith@techcorp.com")
    test_pass_1 = "SecureP@ss1"
    test_pass_2 = "techcorpSecret9!"
    test_pass_3 = "alice99!B@by"
    print(validator.validate(test_pass_1))
    print(validator.validate(test_pass_2))
    print(validator.validate(test_pass_3))