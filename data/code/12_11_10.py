import phonenumbers
from phonenumbers import PhoneNumberType

def validate_phone_numbers(number_list):
    results = []
    for number_str in number_list:
        try:
            parsed_number = phonenumbers.parse(number_str, None)
            if phonenumbers.is_valid_number(parsed_number):
                region_code = phonenumbers.region_code_for_number(parsed_number)
                number_type = phonenumbers.number_type(parsed_number)
                type_name = PhoneNumberType.name_for_number_type(number_type)
                results.append({
                    "original": number_str,
                    "valid": True,
                    "country_code": parsed_number.country_code,
                    "region": region_code,
                    "type": type_name
                })
            else:
                results.append({
                    "original": number_str,
                    "valid": False,
                    "country_code": None,
                    "region": None,
                    "type": None
                })
        except phonenumbers.NumberParseException:
            results.append({
                "original": number_str,
                "valid": False,
                "country_code": None,
                "region": None,
                "type": None
            })
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+14155552671",
        "+442071838750",
        "+33123456789",
        "invalid_number",
        "123",
        "+8613800138000"
    ]
    validation_results = validate_phone_numbers(sample_numbers)
    print(validation_results)