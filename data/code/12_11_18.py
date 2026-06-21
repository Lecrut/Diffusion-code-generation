import phonenumbers
from phonenumbers import PhoneNumberFormat, PhoneNumberType

PHONE_BOOK = [
    "+14155552671",
    "+442071234567",
    "+33142681234",
    "+81312345678",
    "invalid_number",
    "+1234567890",
    "+61412345678",
    "+4915123456789",
]

def analyze_phone_record(raw_input):
    parsed = None
    try:
        parsed = phonenumbers.parse(raw_input, None)
    except phonenumbers.NumberParseException:
        return {
            "original": raw_input,
            "valid": False,
            "country_code": None,
            "format": None
        }

    is_valid = phonenumbers.is_valid_number(parsed)
    
    if is_valid:
        country_code = parsed.country_code
        formatted = phonenumbers.format_number(parsed, PhoneNumberFormat.INTERNATIONAL)
        type_name = PhoneNumberType.Name(phonenumbers.number_type(parsed))
        return {
            "original": raw_input,
            "valid": True,
            "country_code": country_code,
            "format": formatted,
            "type": type_name
        }
    else:
        region = phonenumbers.region_code_for_number(parsed)
        return {
            "original": raw_input,
            "valid": False,
            "country_code": parsed.country_code,
            "format": None
        }

def process_batch(records):
    return [analyze_phone_record(rec) for rec in records]

if __name__ == '__main__':
    results = process_batch(PHONE_BOOK)
    for res in results:
        print(res)