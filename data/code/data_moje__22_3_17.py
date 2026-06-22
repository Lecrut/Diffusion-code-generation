def is_password_compromised(password: str) -> bool:
    common_passwords = {
        "123456", "password", "12345678", "qwerty", "123456789",
        "12345", "1234", "111111", "1234567", "dragon", "123123",
        "baseball", "abc123", "football", "monkey", "letmein",
        "shadow", "master", "666666", "qwertyuiop", "123321",
        "mustang", "121212", "000000", "michael", "654321",
        "pussy", "superman", "1qaz2wsx", "7777777", "888888",
        "123qwe", "killer", "trustno1", "jordan", "jennifer",
        "zxcvbnm", "asdfgh", "hunter", "buster", "soccer",
        "harley", "andrew", "tigger", "charlie", "samantha",
        "barbie", "chelsea", "lovely", "jessica", "ginger",
        "hottie", "love", "princess", "amanda", "joshua",
        "thomas", "matthew", "joseph", "daniel", "william",
        "david", "richard", "robert", "james", "john", "michael",
        "p@ssw0rd", "P@ssword", "Password1", "admin", "welcome",
        "welcome1", "welcome123", "login", "password1", "iloveyou"
    }
    return password in common_passwords

if __name__ == '__main__':
    passwords_to_check = ["securePassword!123", "123456", "MyP@ssw0rd"]
    results = []
    for pwd in passwords_to_check:
        is_compromised = is_password_compromised(pwd)
        results.append({"password": pwd, "is_compromised": is_compromised})
    print(results)