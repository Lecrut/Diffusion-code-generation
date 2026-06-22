def validate_phone_number(phone):
    stripped = ''.join(char for char in phone if char.isdigit())
    if len(stripped) == 11:
        return stripped
    return None

if __name__ == '__main__':
    sample_inputs = ["+1 (555) 123-4567", "123-456-7890", "12345678901", "123456789"]
    for s in sample_inputs:
        result = validate_phone_number(s)
        print(f"{s} -> {result}")