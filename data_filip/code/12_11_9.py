import phonenumbers

NUMBERS = [
    "+12025551234",
    "+442071234567",
    "+33142681234",
    "12025551234",
    "invalid_number",
    "+999123456789012"
]

def validate_phone(number_str):
    try:
        parsed = phonenumbers.parse(number_str, None)
        valid = phonenumbers.is_valid_number(parsed)
        country_code = parsed.country_code
        region = phonenumbers.region_code_for_number(parsed)
        formatted = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        return {
            "input": number_str,
            "valid": valid,
            "country_code": country_code,
            "region": region,
            "formatted": formatted
        }
    except phonenumbers.NumberParseException:
        return {
            "input": number_str,
            "valid": False,
            "country_code": None,
            "region": None,
            "formatted": None
        }

if __name__ == '__main__':
    results = [validate_phone(num) for num in NUMBERS]
    for res in results:
        print(res)