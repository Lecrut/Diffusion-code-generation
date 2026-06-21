import phonenumbers
from phonenumbers import PhoneNumberFormat, NumberParseException

def validate_phone_numbers(phone_number_strings):
    results = []
    for number_str in phone_number_strings:
        try:
            parsed_number = phonenumbers.parse(number_str, None)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            country_code = parsed_number.country_code
            national_number = parsed_number.national_number
            formatted_international = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
            results.append({
                "original": number_str,
                "valid": is_valid,
                "country_code": country_code,
                "national_number": national_number,
                "formatted": formatted_international
            })
        except NumberParseException:
            results.append({
                "original": number_str,
                "valid": False,
                "country_code": None,
                "national_number": None,
                "formatted": None
            })
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+14155552671",
        "+442071838750",
        "+81312345678",
        "invalid_number_xyz",
        "+33123456789"
    ]
    validation_results = validate_phone_numbers(sample_numbers)
    for result in validation_results:
        print(result)