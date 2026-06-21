import re

def validate_e164(phone_number):
    pattern = r'^\+[1-9]\d{1,14}$'
    if re.match(pattern, phone_number):
        return True
    return False

if __name__ == '__main__':
    samples = ['+12025551234', '+44 20 7946 0958', '+33 1 42 68 53 00', 'invalid', '+01234567890', '12025551234']
    results = [validate_e164(sample) for sample in samples]
    print(results)