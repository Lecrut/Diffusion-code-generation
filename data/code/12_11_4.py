import phonenumbers

def validate_phone_numbers(phone_numbers):
    results = []
    for number in phone_numbers:
        try:
            parsed = phonenumbers.parse(number, None)
            is_valid = phonenumbers.is_valid_number(parsed)
            country_code = phonenumbers.region_code_for_number(parsed)
            international_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            national_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            results.append({
                'input': number,
                'valid': is_valid,
                'country_code': country_code,
                'international': international_format,
                'national': national_format
            })
        except phonenumbers.NumberParseException:
            results.append({
                'input': number,
                'valid': False,
                'country_code': None,
                'international': None,
                'national': None
            })
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+14155552671",
        "+442079460958",
        "+8613912345678",
        "invalid_number",
        "+919876543210",
        "+4930123456789",
        "+33123456789",
        "+61412345678",
        "123-456-7890",
        "+5511999999999"
    ]
    results = validate_phone_numbers(sample_numbers)
    for result in results:
        print(result)