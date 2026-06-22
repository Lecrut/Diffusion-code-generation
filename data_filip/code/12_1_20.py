def clean_phone_number(phone: str) -> str:
    return ''.join(char for char in phone if char.isdigit())

def check_phone_length(phone: str) -> bool:
    cleaned = clean_phone_number(phone)
    return len(cleaned) == 11

if __name__ == '__main__':
    sample_numbers = [
        "+1 (555) 123-4567",
        "555-123-4567",
        "123",
        "5551234567890",
        "invalid!@#"
    ]
    for number in sample_numbers:
        result = check_phone_length(number)
        print(result)