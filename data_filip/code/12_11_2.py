import phonenumbers
from phonenumbers import PhoneNumberType

def validate_and_format_numbers(phone_numbers):
    results = []
    for number_str in phone_numbers:
        try:
            parsed_number = phonenumbers.parse(number_str, None)
            if phonenumbers.is_valid_number(parsed_number):
                country_code = parsed_number.country_code
                national_number = parsed_number.national_number
                formatted_national = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
                formatted_international = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                number_type = PhoneNumberType.name(phonenumbers.number_type(parsed_number))
                results.append({
                    "original": number_str,
                    "valid": True,
                    "country_code": country_code,
                    "formatted_national": formatted_national,
                    "formatted_international": formatted_international,
                    "type": number_type
                })
            else:
                results.append({
                    "original": number_str,
                    "valid": False,
                    "country_code": None,
                    "formatted_national": None,
                    "formatted_international": None,
                    "type": None
                })
        except phonenumbers.NumberParseException:
            results.append({
                "original": number_str,
                "valid": False,
                "country_code": None,
                "formatted_national": None,
                "formatted_international": None,
                "type": None
            })
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+14155552671",
        "+442071838750",
        "+33144424200",
        "invalid_number",
        "+81312345678",
        "0000000000"
    ]
    output = validate_and_format_numbers(sample_numbers)
    for item in output:
        print(item)