import phonenumbers

def validate_phone_numbers(phone_numbers):
    results = []
    for number in phone_numbers:
        try:
            parsed = phonenumbers.parse(number, None)
            is_valid = phonenumbers.is_valid_number(parsed)
            if is_valid:
                country_code = phonenumbers.region_code_for_number(parsed)
                formatted = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                results.append({
                    "original": number,
                    "valid": True,
                    "country_code": country_code,
                    "formatted": formatted
                })
            else:
                results.append({
                    "original": number,
                    "valid": False,
                    "country_code": None,
                    "formatted": None
                })
        except phonenumbers.NumberParseException:
            results.append({
                "original": number,
                "valid": False,
                "country_code": None,
                "formatted": None
            })
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+14155552671",
        "+442071838750",
        "+919876543210",
        "+8613800138000",
        "+4930123456",
        "+61298765432",
        "invalid_number",
        "+33123456789",
        "+5511999998888",
        "+81312345678"
    ]
    validation_results = validate_phone_numbers(sample_numbers)
    print(validation_results)