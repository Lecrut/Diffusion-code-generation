import phonenumbers
from phonenumbers import PhoneNumberType
from typing import List, Dict, Any

class PhoneNumberValidator:
    def __init__(self, numbers: List[str]):
        self.numbers = numbers
        self.results = []

    def validate(self) -> List[Dict[str, Any]]:
        for raw_number in self.numbers:
            try:
                parsed_number = phonenumbers.parse(raw_number, None)
                is_valid = phonenumbers.is_valid_number(parsed_number)
                country_code = parsed_number.country_code
                number_type = PhoneNumberType.name(parsed_number.number_type)
                e164_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                result = {
                    "raw": raw_number,
                    "is_valid": is_valid,
                    "country_code": country_code,
                    "type": number_type,
                    "e164": e164_format,
                    "international": international_format
                }
            except phonenumbers.NumberParseException:
                result = {
                    "raw": raw_number,
                    "is_valid": False,
                    "country_code": None,
                    "type": None,
                    "e164": None,
                    "international": None
                }
            self.results.append(result)
        return self.results

if __name__ == '__main__':
    sample_numbers = [
        "+1 555 236 8000",
        "0491 570 156",
        "+44 20 7946 0958",
        "123456",
        "+81 3-1234-5678",
        "+49 15123456789"
    ]
    validator = PhoneNumberValidator(sample_numbers)
    validation_results = validator.validate()
    print(validation_results)