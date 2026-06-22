def has_non_alphanumeric_non_space(s):
    for char in s:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_string = "Hello World! How are you?"
    result = has_non_alphanumeric_non_space(sample_string)
    print(result)