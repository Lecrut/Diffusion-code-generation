import re

validate_mobile = lambda phone: bool(re.match(r'^\+?1?\d{9,15}$', phone.strip()))

if __name__ == '__main__':
    samples = ['+1234567890', '1234567890', '23456789', '+442079460958', 'abc123', '+12345']
    results = [validate_mobile(s) for s in samples]
    print(dict(zip(samples, results)))