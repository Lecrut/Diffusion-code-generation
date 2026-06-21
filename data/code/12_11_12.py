import phonenumbers
from phonenumbers import PhoneNumberFormat, NumberParseException

def validate_and_extract(phone_numbers):
    results = []
    for number_str in phone_numbers:
        try:
            parsed_number = phonenumbers.parse(number_str, None)
            if phonenumbers.is_valid_number(parsed_number):
                country_code = parsed_number.country_code
                national_number = parsed_number.national_number
                formatted_national = phonenumbers.format_number(parsed_number, PhoneNumberFormat.NATIONAL)
                formatted_international = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
                results.append({
                    "input": number_str,
                    "is_valid": True,
                    "country_code": country_code,
                    "national_number": national_number,
                    "formatted_national": formatted_national,
                    "formatted_international": formatted_international
                })
            else:
                results.append({
                    "input": number_str,
                    "is_valid": False,
                    "country_code": None,
                    "national_number": None,
                    "formatted_national": None,
                    "formatted_international": None
                })
        except NumberParseException:
            results.append({
                "input": number_str,
                "is_valid": False,
                "country_code": None,
                "national_number": None,
                "formatted_national": None,
                "formatted_international": None
            })
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+14155552671",
        "+442071838750",
        "+4930123456",
        "123-456-7890",
        "+8613800138000"
    ]
    output = validate_and_extract(sample_numbers)
    for item in output:
        print(item)