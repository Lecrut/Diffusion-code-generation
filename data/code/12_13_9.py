import re

PATTERN = re.compile(r"^\+?\d{10,14}$")

def validate_phone_list(numbers):
    cleaned = []
    for n in numbers:
        digits = re.sub(r"\D", "", n)
        if n.startswith("+"):
            digits = "+" + digits
        if PATTERN.match(digits):
            cleaned.append(n)
    return cleaned

if __name__ == '__main__':
    data = ["+1 555 123 4567", "(555) 123-4567", "5551234567", "123456789012", "bad number", "+1 23 4567"]
    result = validate_phone_list(data)
    print(result)