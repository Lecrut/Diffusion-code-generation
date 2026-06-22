def process_phone_number(phone_number: str) -> bool:
    digits = ''.join(char for char in phone_number if char.isdigit())
    return len(digits) == 11

if __name__ == '__main__':
    sample_numbers = [
        "+1 (555) 123-4567",
        "5551234567",
        "123-456-78901",
        "010-1234-5678",
        "555 123 4567"
    ]
    for number in sample_numbers:
        result = process_phone_number(number)
        print(result)