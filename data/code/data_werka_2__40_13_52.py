import re

def find_first_letter(text):
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

if __name__ == '__main__':
    test_cases = [
        "No letters here!",
        "1234567890",
        "A quick brown fox",
        "",
        "Special!@#$$%^&*()"
    ]
    for case in test_cases:
        first_letter = find_first_letter(case)
        print(first_letter)