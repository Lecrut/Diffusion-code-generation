def filter_phone_numbers(numbers):
    result = []
    for number in numbers:
        if number.isdigit() and len(number) == 10:
            result.append(number)
    return result

if __name__ == '__main__':
    sample_numbers = ["1234567890", "987-654-3210", "5551234567", "12345", "9876543210", "abc1234567"]
    print(filter_phone_numbers(sample_numbers))