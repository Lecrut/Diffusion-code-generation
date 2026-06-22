import phonenumbers
SAMPLE_NUMBERS = ['+14155552671', '+442071838750', '447700900123', '+81312345678', '+919876543210', '+33123456789', '1234567890', '+4930123456', 'invalid_number', '']

def validate_phone_numbers(numbers: list) -> list:
    results = []
    for num_str in numbers:
        try:
            parsed_number = phonenumbers.parse(num_str, None)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            country_code = parsed_number.country_code
            number_type = phonenumbers.number_type(parsed_number)
            national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
            international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            result_entry = {'original': num_str, 'valid': is_valid, 'country_code': country_code, 'national_format': national_format, 'international_format': international_format, 'type': str(number_type), 'region': phonenumbers.region_code_for_number(parsed_number)}
        except phonenumbers.NumberParseException:
            result_entry = {'original': num_str, 'valid': False, 'country_code': None, 'national_format': None, 'international_format': None, 'type': 'ERROR', 'region': None}
        results.append(result_entry)
    return results
if __name__ == '__main__':
    results = validate_phone_numbers(SAMPLE_NUMBERS)
    for item in results:
        print(item)