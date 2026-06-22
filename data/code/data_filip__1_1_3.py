import re

def validate_email(email):
    if not isinstance(email, str):
        return False
    pattern = re.compile(
        r"^(?!.*\.\.)(?!.*\.$)(?!^\.)"
        r"[a-zA-Z0-9_.+-]+"
        r"@"
        r"(?=[a-zA-Z0-9-]{1,63}\.)"
        r"[a-zA-Z0-9-]+"
        r"\.[a-zA-Z]{2,}$"
    )
    return bool(pattern.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "valid.name+tag@sub.domain.org",
        "invalid..email@test.com",
        "no-at-symbol.com",
        "missing@domain",
        "trailing.@test.com",
        "good_user123@mail.server.net"
    ]
    results = []
    for email in test_emails:
        result = validate_email(email)
        results.append(result)
    print(results)