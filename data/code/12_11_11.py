import phonenumbers
from phonenumbers import PhoneNumberFormat, PhoneNumberType

PHONE_NUMBERS = [
    "+14155552671",
    "+44 20 7946 0958",
    "+33 1 42 68 53 00",
    "invalid_phone",
    "+81 3 1234 5678",
    "+61 2 9876 5432",
    "+86 10 1234 5678",
    "+91 11 2345 6789",
    "+55 11 98765 4321",
    "+49 30 12345678",
]

def validate_phone_number(phone_string: str) -> dict:
    try:
        parsed_number = phonenumbers.parse(phone_string, None)
        if phonenumbers.is_valid_number(parsed_number):
            country_code = parsed_number.country_code
            region = phonenumbers.region_code_for_number(parsed_number)
            number_type = phonenumbers.number_type(parsed_number)
            formatted_number = phonenumbers.format_number(
                parsed_number, PhoneNumberFormat.INTERNATIONAL
            )
            return {
                "is_valid": True,
                "country_code": country_code,
                "region": region,
                "type": number_type,
                "formatted": formatted_number,
            }
        else:
            return {
                "is_valid": False,
                "country_code": None,
                "region": None,
                "type": None,
                "formatted": None,
            }
    except phonenumbers.NumberParseException:
        return {
            "is_valid": False,
            "country_code": None,
            "region": None,
            "type": None,
            "formatted": None,
        }

def validate_phone_array(phone_list: list) -> list:
    results = []
    for phone in phone_list:
        result = validate_phone_number(phone)
        results.append(result)
    return results

if __name__ == '__main__':
    phone_list = PHONE_NUMBERS
    results = validate_phone_array(phone_list)
    for result in results:
        print(result)