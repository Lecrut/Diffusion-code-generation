import re

def validate_password(password):
    return bool(re.search(r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\-]).{8,}$', password))

if __name__ == '__main__':
    print(validate_password("Short1!"))
    print(validate_password("LongEnough1!"))
    print(validate_password("NoDigit!A"))
    print(validate_password("NoUpper1!"))
    print(validate_password("NoSpecial1A"))
    print(validate_password("Valid123!A"))