def filter_phone_numbers(numbers):
    result = []
    for number in numbers:
        cleaned = "".join(c for c in number if c.isdigit())
        if len(cleaned) == 10 and cleaned.isdigit():
            result.append(cleaned)
    return result

if __name__ == '__main__':
    sample_data = ["123-456-7890", "(123) 456-7890", "123456789", "12345678901", "123 456 7890", "abc-def-ghij"]
    print(filter_phone_numbers(sample_data))