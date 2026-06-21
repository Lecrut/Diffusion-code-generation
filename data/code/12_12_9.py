class PhoneValidator:
    @staticmethod
    def is_valid(phone: str) -> dict:
        import re
        pattern = r'^\+[1-9]\d{1,14}$'
        is_valid = bool(re.match(pattern, phone))
        return {
            'number': phone,
            'is_valid': is_valid,
            'country_code': None if not is_valid else int(phone[1:].split('0')[0]) if '0' in phone[1:] else int(phone[1:]) if not phone[1:].startswith('0') else None
        }

if __name__ == '__main__':
    phone_list = ["+12065551234", "+447911123456", "+1234", "+", "+12065551234567890", "+61412345678"]
    results = [PhoneValidator.is_valid(p) for p in phone_list]
    for result in results:
        print(result)