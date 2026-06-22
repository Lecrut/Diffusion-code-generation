import re
import socket

EMAIL_REGEX = re.compile(r'^(?!.*\.\.)(?!.*\.$)^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

def validate_emails(email_list):
    results = {}
    for email in email_list:
        is_valid = False
        reason = ""
        
        if EMAIL_REGEX.match(email):
            parts = email.split('@')
            local_part = parts[0]
            domain = parts[1]
            
            valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")
            if all(char in valid_chars for char in local_part):
                try:
                    socket.gethostbyname(domain)
                    is_valid = True
                    reason = "Valid"
                except socket.gaierror:
                    is_valid = False
                    reason = "Invalid DNS"
            else:
                is_valid = False
                reason = "Invalid local-part characters"
        else:
            is_valid = False
            reason = "Regex mismatch"
        
        results[email] = {"valid": is_valid, "reason": reason}
    
    return results

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "user.name@sub.domain.co.uk",
        "invalid@.com",
        "bad..char@test.com",
        "valid_user+tag@server.org",
        "missing@domain",
        "@missinglocal.com",
        "no-at-symbol.com"
    ]
    
    output = validate_emails(test_emails)
    for email, info in output.items():
        print(f"{email}: {info}")