import re

def validate_phone_number(phone_number):
    stripped_digits = re.sub(r'\D', '', phone_number)
    if len(stripped_digits) == 11:
        return stripped_digits
    return None

if __name__ == '__main__':
    test_input_1 = "+1 (555) 123-4567"
    test_input_2 = "9876543210"
    test_input_3 = "123-456-78901"
    print(validate_phone_number(test_input_1))
    print(validate_phone_number(test_input_2))
    print(validate_phone_number(test_input_3))