def is_compromised(password: str) -> bool:
    compromised_passwords = frozenset({
        "123456", "password", "12345678", "qwerty", "abc123",
        "monkey", "1234567", "letmein", "trustno1", "dragon",
        "baseball", "iloveyou", "master", "sunshine", "ashley",
        "bailey", "passw0rd", "shadow", "123123", "654321",
        "superman", "qazwsx", "michael", "football", "password1"
    })
    lower_password = password.lower()
    return lower_password in compromised_passwords

if __name__ == '__main__':
    test_passwords = ["SuperSecret123", "123456", "MyDogLovesTreats", "password"]
    results = {}
    for pwd in test_passwords:
        results[pwd] = is_compromised(pwd)
    print(results)