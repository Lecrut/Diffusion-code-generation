import re

validate_phone = lambda phone: bool(re.fullmatch(r'\+?[1-9]\d{1,14}', phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')))

if __name__ == '__main__':
    sample1 = "+1-415-555-2671"
    sample2 = "invalid"
    sample3 = "+44 20 7946 0958"
    print(validate_phone(sample1))
    print(validate_phone(sample2))
    print(validate_phone(sample3))