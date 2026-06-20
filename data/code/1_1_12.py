import re

def validate_email(address):
    if not address or not isinstance(address, str):
        return False
    pattern = r"^(?=[a-zA-Z0-9._%+-]{1,64}@)(?=[a-zA-Z0-9.-]{1,255}$)(?=(?:[a-zA-Z0-9]{2,})@)(?=(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, address))

if __name__ == "__main__":
    samples = [
        "user@example.com",
        "invalid.email",
        "name@domain.co.uk",
        "@missinglocal.com",
        "missing@domain",
        "spaces @bad.com"
    ]
    for email in samples:
        print(validate_email(email))