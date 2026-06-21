import phonenumbers
from phonenumbers import PhoneNumberFormat

def validate_phones(phone_numbers):
    results = []
    for phone_str in phone_numbers:
        try:
            parsed = phonenumbers.parse(phone_str, None)
            is_valid = phonenumbers.is_valid_number(parsed)
            country_code = parsed.country_code
            if is_valid:
                formatted = phonenumbers.format_number(parsed, PhoneNumberFormat.INTERNATIONAL)
                format_status = "INTERNATIONAL"
            else:
                formatted = phone_str
                format_status = "INVALID"
            results.append({
                "number": phone_str,
                "valid": is_valid,
                "country_code": country_code,
                "formatted": formatted,
                "format_status": format_status
            })
        except phonenumbers.NumberParseException:
            results.append({
                "number": phone_str,
                "valid": False,
                "country_code": None,
                "formatted": phone_str,
                "format_status": "PARSE_ERROR"
            })
    return results

if __name__ == '__main__':
    sample_phones = [
        "+14155552671",
        "+442071234567",
        "invalid_number",
        "+33123456789"
    ]
    
    results = validate_phones(sample_phones)
    
    for res in results:
        print(res)