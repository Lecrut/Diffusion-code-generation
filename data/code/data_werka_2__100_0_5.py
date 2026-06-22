def validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    return value

def check_sign(value):
    validated = validate_numeric(value)
    if validated > 0:
        return "positive"
    if validated < 0:
        return "negative"
    return "zero"

if __name__ == '__main__':
    print(check_sign(15))
    print(check_sign(-20))
    print(check_sign(0))