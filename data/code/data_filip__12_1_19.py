import re

def validate_phone_number(phone_number):
    digits = re.sub(r'\D', '', phone_number)
    return len(digits) == 11

if __name__ == '__main__':
    sample_1 = "123-456-7890-1"
    sample_2 = "1234567890"
    sample_3 = "987-654-3210-12"
    result_1 = validate_phone_number(sample_1)
    result_2 = validate_phone_number(sample_2)
    result_3 = validate_phone_number(sample_3)
    print(result_1)
    print(result_2)
    print(result_3)