import phonenumbers
from phonenumbers import PhoneNumberFormat, PhoneNumberType

def validate_phone_numbers(numbers):
    results = []
    for num_str in numbers:
        try:
            parsed = phonenumbers.parse(num_str, None)
            if phonenumbers.is_valid_number(parsed):
                country_code = parsed.country_code
                format_status = phonenumbers.format_number(parsed, PhoneNumberFormat.INTERNATIONAL)
                number_type = PhoneNumberType(parsed.type_if_known())
                results.append({
                    'original': num_str,
                    'valid': True,
                    'country_code': country_code,
                    'formatted': format_status,
                    'type': str(number_type)
                })
            else:
                results.append({
                    'original': num_str,
                    'valid': False,
                    'country_code': None,
                    'formatted': None,
                    'type': 'INVALID'
                })
        except phonenumbers.NumberParseException:
            results.append({
                'original': num_str,
                'valid': False,
                'country_code': None,
                'formatted': None,
                'type': 'PARSE_ERROR'
            })
    return results

if __name__ == '__main__':
    samples = [
        "+14155552671",
        "+44 20 7946 0958",
        "+91 98765 43210",
        "123456789",
        "+61 4 1234 5678"
    ]
    output = validate_phone_numbers(samples)
    print(output)