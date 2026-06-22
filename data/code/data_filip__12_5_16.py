def validate_phone_number(phone: str) -> bool:
    if not phone or not phone.startswith('+'):
        return False
    
    rest = phone[1:]
    if not rest.isdigit():
        return False
    
    parts = rest.split()
    
    if len(parts) != 2:
        country_code = parts[0]
        phone_part = parts[1] if len(parts) > 1 else ""
        
        if not phone_part.isdigit():
            return False
            
        if not (1 <= len(country_code) <= 3):
            return False
            
        if not (7 <= len(phone_part) <= 10):
            return False
            
        return True
    
    if len(parts) == 1:
        country_code = parts[0]
        if not country_code.isdigit():
            return False
        
        if not (1 <= len(country_code) <= 3):
            return False
            
        if not (7 <= len(country_code) <= 10):
            return False
            
        return True

    if len(parts) >= 2:
        country_code = parts[0]
        phone_part = ''.join(parts[1:])
        
        if not country_code.isdigit():
            return False
        
        if not (1 <= len(country_code) <= 3):
            return False
            
        if not phone_part.isdigit():
            return False
            
        if not (7 <= len(phone_part) <= 10):
            return False
            
        return True
    
    return False

if __name__ == '__main__':
    print(validate_phone_number("+15551234567"))
    print(validate_phone_number("+919876543210"))
    print(validate_phone_number("15551234567"))
    print(validate_phone_number("+1555"))
    print(validate_phone_number("+1234567"))