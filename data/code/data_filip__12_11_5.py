import phonenumbers

def validate_phone_numbers(phone_numbers):
    results = []
    for number in phone_numbers:
        try:
            parsed = phonenumbers.parse(number, None)
            is_valid = phonenumbers.is_valid_number(parsed)
            country_code = phonenumbers.country_code_for_region(
                phonenumbers.region_code_for_number(parsed)
            )
            national_format = phonenumbers.format_number(
                parsed, phonenumbers.PhoneNumberFormat.NATIONAL
            )
            international_format = phonenumbers.format_number(
                parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
            results.append({
                "original": number,
                "valid": is_valid,
                "country_code": country_code,
                "national_format": national_format,
                "international_format": international_format,
            })
        except phonenumbers.NumberParseException:
            results.append({
                "original": number,
                "valid": False,
                "country_code": None,
                "national_format": None,
                "international_format": None,
            })
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+14155552671",
        "+442071838750",
        "+861012345678",
        "+33123456789",
        "invalid-number",
        "+71234567890",
        "+61293715555",
    ]
    validation_results = validate_phone_numbers(sample_numbers)
    print(validation_results)