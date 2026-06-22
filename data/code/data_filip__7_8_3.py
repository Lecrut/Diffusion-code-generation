import re

def analyze_special_chars(s):
    if not s:
        return 0, False
    count = 0
    for char in s:
        if not char.isalnum() and not char.isspace():
            count += 1
    return count, count > 0

if __name__ == '__main__':
    test_string = "Hello, World! 123 @#$"
    result_count, result_status = analyze_special_chars(test_string)
    print((result_count, result_status))
    test_string2 = "JustLetters123"
    result_count2, result_status2 = analyze_special_chars(test_string2)
    print((result_count2, result_status2))