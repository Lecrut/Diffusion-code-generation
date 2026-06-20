def is_valid_input(s):
    if not s:
        return False
    if not s.isalpha():
        return False
    return True

if __name__ == '__main__':
    sample_values = ["HelloWorld", "", "12345", "Python3"]
    for value in sample_values:
        result = is_valid_input(value)
        print(f"'{value}' is valid: {result}")