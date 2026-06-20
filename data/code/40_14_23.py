import re

def find_first_letter(text):
    if not text:
        return None
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

if __name__ == '__main__':
    print(find_first_letter('   123abc'))
    print(find_first_letter(''))
    print(find_first_letter('12345'))
    print(find_first_letter('Hello'))
    print(find_first_letter('...!!!@#@'))