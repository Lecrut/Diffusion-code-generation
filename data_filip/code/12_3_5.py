import re

def is_valid_us_phone(number: str) -> bool:
    pattern = r'^\(?1?\)?[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$'
    if not re.match(pattern, number):
        return False
    
    digits = ''.join(filter(str.isdigit, number))
    
    if len(digits) == 10:
        return True
    
    if len(digits) == 11 and digits[0] == '1':
        return True
        
    return False

if __name__ == '__main__':
    sample_phones = ['(123) 456-7890', '123-456-7890', '1234567890', '1-123-456-7890', '123 456 7890', '(123)456-7890', '123-45-6789']
    results = [is_valid_us_phone(phone) for phone in sample_phones]
    print(results)