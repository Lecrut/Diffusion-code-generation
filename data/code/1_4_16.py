import re

class EmailValidator:
    @staticmethod
    def is_valid(email):
        if not isinstance(email, str):
            return False
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

if __name__ == '__main__':
    validator = EmailValidator()
    test_email = "user.name+tag@example.co.uk"
    result = validator.is_valid(test_email)
    print(result)
    invalid_email = "user@invalid"
    invalid_result = validator.is_valid(invalid_email)
    print(invalid_result)