import re

def validate_phone_numbers(numbers):
    pattern = re.compile(r'^[\+]?[(]?[0-9]{1,4}[)]?[-\s\.]?[0-9]{1,4}[-\s\.]?[0-9]{1,9}$')
    normalized = []
    for num in numbers:
        clean = ''.join(c for c in num if c.isdigit() or c in '+-().')
        if pattern.match(clean):
            normalized.append(clean)
    return normalized

if __name__ == '__main__':
    sample_numbers = [
        "+1 (555) 123-4567",
        "555.123.4567",
        "123-ABC-5678",
        "12345678901",
        "(555) 1234567",
        "invalid number",
        "+44 20 1234 5678"
    ]
    result = validate_phone_numbers(sample_numbers)
    print(result)