def process_phone_number(phone_str: str) -> int:
    digits = ''.join(c for c in phone_str if c.isdigit())
    if len(digits) != 11:
        return -1
    return int(digits)

if __name__ == '__main__':
    sample_numbers = [
        "123-456-7890",
        "+1 (234) 567-8901",
        "01234567890",
        "12345"
    ]
    results = [process_phone_number(s) for s in sample_numbers]
    for s, r in zip(sample_numbers, results):
        print(r)