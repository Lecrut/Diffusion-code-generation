import re

def validate_phone_numbers(numbers):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    normalized = []
    for num in numbers:
        clean = re.sub(r'\D', '', num)
        if pattern.match(clean):
            normalized.append(clean)
    return normalized

if __name__ == '__main__':
    samples = [
        "+1-202-555-0173",
        "(310) 555-0199",
        "202.555.0120",
        "invalid-number",
        "555-0199",
        "+44 20 7946 0958"
    ]
    result = validate_phone_numbers(samples)
    print(result)