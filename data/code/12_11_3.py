import phonenumbers

def validate_international_phones(phone_strings):
    results = []
    for phone_str in phone_strings:
        try:
            parsed_number = phonenumbers.parse(phone_str, None)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            region_code = phonenumbers.region_code_for_number(parsed_number)
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            country_code = parsed_number.country_code
            results.append({
                'input': phone_str,
                'valid': is_valid,
                'region_code': region_code,
                'formatted': formatted_number,
                'country_code': country_code
            })
        except phonenumbers.NumberParseException:
            results.append({
                'input': phone_str,
                'valid': False,
                'region_code': None,
                'formatted': None,
                'country_code': None
            })
    return results

if __name__ == '__main__':
    sample_phones = [
        "+14155552671",
        "+442071838750",
        "+81312345678",
        "+12025550178",
        "invalid_phone"
    ]
    
    validation_results = validate_international_phones(sample_phones)
    for result in validation_results:
        print(result)