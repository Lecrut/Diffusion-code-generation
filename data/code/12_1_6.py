def format_phone_number(phone_string: str) -> str:
    digits = ''.join(char for char in phone_string if char.isdigit())
    if len(digits) == 11:
        return digits
    return ''

if __name__ == '__main__':
    sample_values = [
        "+1 (555) 123-4567",
        "5551234567890",
        "555-1234",
        "12345678901"
    ]
    for val in sample_values:
        result = format_phone_number(val)
        print(result)