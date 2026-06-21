import re

def validate_password(username: str, email: str, password: str) -> bool:
    if len(password) < 8:
        return False

    email_domain = email.split('@')[-1].lower() if '@' in email else email.lower()
    username_lower = username.lower()
    password_lower = password.lower()

    if username_lower in password_lower:
        return False

    if email_domain and email_domain in password_lower:
        return False

    return True

if __name__ == '__main__':
    result = validate_password("john_doe", "john@securemail.com", "P@ssw0rd!")
    print(result)