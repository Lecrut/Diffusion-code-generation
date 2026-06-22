import re

VALID_LOCAL_PART = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def validate_emails(email_list):
    results = []
    for email in email_list:
        if VALID_LOCAL_PART.match(email):
            domain_parts = email.split("@")
            if len(domain_parts) == 2:
                local_part, domain = domain_parts
                domain_name = domain.split(".")[0]
                if len(domain_name) > 0:
                    results.append(True)
                    continue
        results.append(False)
    return results

if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "user.name@sub.domain.co.uk",
        "invalid-email@",
        "@invalid.com",
        "user@invalid",
        "user+tag@valid.org"
    ]
    output = validate_emails(test_emails)
    print(output)