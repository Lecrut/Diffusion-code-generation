import phonenumbers

PHONE_NUMBERS = [
    "+14155552671",
    "+442071838750",
    "+81312345678",
    "invalid_number",
    "+919876543210",
    "+61412345678",
    "+33142681234",
    "+4930123456",
    "+5511987654321",
    "+8613800138000"
]

def validate_phone_numbers(numbers):
    results = []
    for number_str in numbers:
        try:
            parsed = phonenumbers.parse(number_str, None)
            is_valid = phonenumbers.is_valid_number(parsed)
            country_code = parsed.country_code
            number_type = phonenumbers.number_type(parsed)
            country = phonenumbers.region_code_for_number(parsed)
            formatted = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            results.append({
                'original': number_str,
                'valid': is_valid,
                'country_code': country_code,
                'country': country,
                'type': str(number_type),
                'international_format': formatted
            })
        except phonenumbers.NumberParseException:
            results.append({
                'original': number_str,
                'valid': False,
                'country_code': None,
                'country': None,
                'type': None,
                'international_format': None
            })
    return results

if __name__ == '__main__':
    results = validate_phone_numbers(PHONE_NUMBERS)
    for r in results:
        print(r)