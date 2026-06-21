import re

validate_phone = lambda phone: bool(re.match(r'^\+?1?\d{9,15}$', phone))

if __name__ == '__main__':
    sample_numbers = ['+14155552671', '4155552671', '415-555-2671', '415.555.2671', 'invalid']
    results = {num: validate_phone(num) for num in sample_numbers}
    print(results)