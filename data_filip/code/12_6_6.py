def validate_phone_number(phone: str) -> bool:
    length = len(phone)
    if length < 7 or length > 15:
        return False
    for char in phone:
        if char.isalpha():
            return False
    return True

if __name__ == '__main__':
    samples = ["1234567", "123-456-7890", "abc1234567", "123456", "1234567890123456", "987654321012345"]
    results = []
    for sample in samples:
        results.append(validate_phone_number(sample))
    print(results)