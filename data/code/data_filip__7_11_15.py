def has_no_special_characters(s):
    return s.isalnum() or s == ""

if __name__ == '__main__':
    sample_values = ["hello123", "hello world", "test@123", "validString42", "special!@#", ""]
    for val in sample_values:
        print(f"{val}: {has_no_special_characters(val)}")