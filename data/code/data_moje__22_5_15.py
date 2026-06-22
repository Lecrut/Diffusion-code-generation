def validate_password(password: str, username: str, email: str) -> bool:
    if not password:
        return False
    
    lower_password = password.lower()
    lower_username = username.lower()
    
    if lower_username and lower_username in lower_password:
        return False
    
    if email and '@' in email:
        domain = email.split('@')[-1]
        lower_domain = domain.lower()
        if lower_domain in lower_password:
            return False
    
    return True

if __name__ == '__main__':
    result1 = validate_password("myPassword123", "john", "john@example.com")
    print(result1)
    
    result2 = validate_password("johnDoe", "john", "john@example.com")
    print(result2)
    
    result3 = validate_password("securePwd!@example.com", "alice", "alice@example.com")
    print(result3)
    
    result4 = validate_password("SafePass", "bob", "bob@test.org")
    print(result4)