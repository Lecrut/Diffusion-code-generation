import phonenumbers
from phonenumbers import phonenumberutil

PHONE_NUMBERS = [
    "+14155552671",
    "+442071234567",
    "+33142681234",
    "+81312345678",
    "invalid_number",
    "+1234567890",
    "+61412345678",
    "+4915123456789",
]

def validate_phone_numbers(numbers):
    results = []
    for num_str in numbers:
        try:
            parsed_number = phonenumbers.parse(num_str, None)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            country_code = parsed_number.country_code
            formatted = None
            if is_valid:
                formatted = phonenumbers.format_number(
                    parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
                )
            results.append({
                "number": num_str,
                "valid": is_valid,
                "country_code": country_code,
                "formatted": formatted
            })
        except phonenumbers.NumberParseException:
            results.append({
                "number": num_str,
                "valid": False,
                "country_code": None,
                "formatted": None
            })
    return results

if __name__ == '__main__':
    output = validate_phone_numbers(PHONE_NUMBERS)
    print(output)