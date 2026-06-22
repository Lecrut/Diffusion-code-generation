import phonenumbers

def validate_phone_numbers(phone_numbers):
    results = []
    for number in phone_numbers:
        try:
            parsed_number = phonenumbers.parse(number, None)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            country_code = phonenumbers.country_code_for_region(
                phonenumbers.region_code_for_number(parsed_number)
            )
            number_type = phonenumbers.number_type(parsed_number)
            type_name = "UNKNOWN"
            if number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                type_name = "FIXED_LINE"
            elif number_type == phonenumbers.PhoneNumberType.MOBILE:
                type_name = "MOBILE"
            elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
                type_name = "FIXED_LINE_OR_MOBILE"
            elif number_type == phonenumbers.PhoneNumberType.TOLL_FREE:
                type_name = "TOLL_FREE"
            elif number_type == phonenumbers.PhoneNumberType.PREMIUM_RATE:
                type_name = "PREMIUM_RATE"
            elif number_type == phonenumbers.PhoneNumberType.SHARED_COST:
                type_name = "SHARED_COST"
            elif number_type == phonenumbers.PhoneNumberType.VOIP:
                type_name = "VOIP"
            elif number_type == phonenumbers.PhoneNumberType.PERSONAL_NUMBER:
                type_name = "PERSONAL_NUMBER"
            elif number_type == phonenumbers.PhoneNumberType.PAGER:
                type_name = "PAGER"
            elif number_type == phonenumbers.PhoneNumberType.UAN:
                type_name = "UAN"
            elif number_type == phonenumbers.PhoneNumberType.VOICEMAIL:
                type_name = "VOICEMAIL"
            
            results.append({
                "original": number,
                "valid": is_valid,
                "country_code": country_code,
                "type": type_name
            })
        except phonenumbers.NumberParseException:
            results.append({
                "original": number,
                "valid": False,
                "country_code": None,
                "type": "PARSE_ERROR"
            })
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+14155552671",
        "+442071838750",
        "+861012345678",
        "+33123456789",
        "invalid-number",
        "+1-415-555-2671",
        "+61412345678"
    ]
    validation_results = validate_phone_numbers(sample_numbers)
    print(validation_results)