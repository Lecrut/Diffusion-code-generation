def check_password_strength(password):
    HAS_LOWER = 0
    HAS_UPPER = 1
    HAS_DIGIT = 2
    HAS_SYMBOL = 3
    LEN_OK = 4
    FLAGS = 0
    length = len(password)
    if length >= 12:
        FLAGS |= (1 << LEN_OK)
    for char in password:
        code = ord(char)
        if code >= 97 and code <= 122:
            FLAGS |= (1 << HAS_LOWER)
        elif code >= 65 and code <= 90:
            FLAGS |= (1 << HAS_UPPER)
        elif code >= 48 and code <= 57:
            FLAGS |= (1 << HAS_DIGIT)
        elif (code >= 33 and code <= 47) or (code >= 58 and code <= 64) or (code >= 91 and code <= 96) or (code >= 123 and code <= 126):
            FLAGS |= (1 << HAS_SYMBOL)
    REQUIRED = (1 << HAS_LOWER) | (1 << HAS_UPPER) | (1 << HAS_DIGIT) | (1 << HAS_SYMBOL) | (1 << LEN_OK)
    return (FLAGS & REQUIRED) == REQUIRED

if __name__ == '__main__':
    test_password = "SecureP@ssw0rd123"
    result = check_password_strength(test_password)
    print(result)
    test_weak = "password"
    weak_result = check_password_strength(test_weak)
    print(weak_result)