import re

def is_valid_e164(phone_number: str) -> bool:
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    test_numbers = [
        "+12025551234",
        "+441234567890",
        "+911234567890123",
        "12025551234",
        "+0123456789",
        "+1234567890123456",
        "+ 12025551234",
        "+1202555",
    ]
    
    results = []
    for number in test_numbers:
        results.append(f"{number}: {is_valid_e164(number)}")
    
    for result in results:
        print(result)