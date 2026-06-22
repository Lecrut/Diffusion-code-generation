def validate_phone_number(phone_str):
    cleaned = "".join(c for c in phone_str if c.isdigit())
    if len(cleaned) == 11:
        return cleaned
    return None

if __name__ == '__main__':
    sample_input_1 = "(555) 123-4567"
    sample_input_2 = "+1 (555) 9876543210"
    sample_input_3 = "1234567890"
    print(validate_phone_number(sample_input_1))
    print(validate_phone_number(sample_input_2))
    print(validate_phone_number(sample_input_3))