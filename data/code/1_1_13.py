import re

def validate_email(email):
    pattern = (
        r'^'
        r'(?=.*[a-zA-Z0-9._%+-]+@)'
        r'(?=.*[a-zA-Z]{2,}\.?[a-zA-Z]*$)'
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        r'$'
    )
    if re.match(pattern, email):
        return True
    return False

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid-email",
        "user@.com",
        "user@com.",
        "user name@example.com",
        "user@exam_ple.com",
        "a.b.c@test.co.uk"
    ]
    results = []
    for sample in samples:
        result = validate_email(sample)
        results.append(result)
    print(results)