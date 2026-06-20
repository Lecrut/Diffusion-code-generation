import re

def analyze_special_chars(text):
    count = 0
    has_special = False
    for char in text:
        if not char.isalnum() and not char.isspace():
            count += 1
            has_special = True
    return count, has_special

if __name__ == '__main__':
    sample_string = "Hello, World! @2024"
    result_count, result_status = analyze_special_chars(sample_string)
    print((result_count, result_status))