import re
import string

class PasswordValidator:

    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False
        special_chars = set(string.punctuation)
        special_in_password = set((char for char in password if char in special_chars))
        if len(special_in_password) < 2:
            return False
        if PasswordValidator._has_sequential_keyboard_pattern(password):
            return False
        return True

    @staticmethod
    def _has_sequential_keyboard_pattern(password):
        keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        lower_password = password.lower()
        for row in keyboard_rows:
            for i in range(len(row) - 2):
                forward_seq = row[i:i + 3]
                backward_seq = forward_seq[::-1]
                if forward_seq in lower_password or backward_seq in lower_password:
                    return True
        return False
if __name__ == '__main__':
    samples = ['short!@', 'longenough12345', 'validP@ssw0rd!##', 'qwerty12345!@', 'secureP@ss123!!', '123456789012!!', 'asdfgh12345!@', 'zxcvbn12345!@', 'Complex!Pass#123', 'NoSpecialsHere1234', 'OneSpecialOnly!1234567890', 'TwoSpecials!@123456789']
    validator = PasswordValidator()
    for sample in samples:
        result = validator.validate(sample)
        print(f'{sample}: {result}')