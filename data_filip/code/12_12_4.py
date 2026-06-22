class PhoneValidator:
    @staticmethod
    def is_valid(phone_number: str) -> dict:
        pattern = r'^\+?[1-9]\d{1,14}$'
        if isinstance(phone_number, str) and phone_number and len(phone_number) <= 15:
            if len(phone_number) > 0 and phone_number[0] == '+':
                digits = phone_number[1:]
                if len(digits) >= 1 and digits.isdigit():
                    first_digit = int(digits[0])
                    if 1 <= first_digit <= 9:
                        return {
                            "number": phone_number,
                            "valid": True,
                            "country_code_present": True,
                            "format_compliant": True
                        }
            elif phone_number.isdigit():
                if 1 <= int(phone_number[0]) <= 9:
                    return {
                        "number": phone_number,
                        "valid": True,
                        "country_code_present": False,
                        "format_compliant": True
                    }
        return {
            "number": phone_number,
            "valid": False,
            "country_code_present": False,
            "format_compliant": False
        }

if __name__ == '__main__':
    validator = PhoneValidator()
    samples = [
        "+12125551212",
        "2125551212",
        "+911234567890",
        "invalid",
        "+0123456789012345",
        "+1234567890123456"
    ]
    for sample in samples:
        result = validator.is_valid(sample)
        print(result)