import re

validate_mobile = lambda phone: bool(re.fullmatch(r'\+?[1-9]\d{1,14}', phone.strip()))

if __name__ == '__main__':
    samples = ['+14155552671', '4155552671', '+442071234567', 'invalid', '+12345678901234567', '']
    results = [validate_mobile(s) for s in samples]
    for phone, valid in zip(samples, results):
        print(f"{phone!r}: {valid}")