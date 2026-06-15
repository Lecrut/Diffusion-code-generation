import re
def check_for_critical(multi_line_string):
    try:
        lines = multi_line_string.encode('utf-8').decode('utf-8').splitlines()
    except UnicodeDecodeError:
        return False
    pattern = r'critical'
    for line in lines:
        if re.search(pattern, line):
            return True
    return False
if __name__ == '__main__':
    sample_string_1 = "This is a normal line.\nAnother line with critical information.\nFinal line."
    sample_string_2 = "No critical words here.\nJust some text."
    sample_string_3 = "A critical error occurred.\nThis line has no issues."
    sample_string_4 = "Line with critical data, possibly with bad encoding: \x80"
    print(f"Sample 1 result: {check_for_critical(sample_string_1)}")
    print(f"Sample 2 result: {check_for_critical(sample_string_2)}")
    print(f"Sample 3 result: {check_for_critical(sample_string_3)}")
    print(f"Sample 4 result: {check_for_critical(sample_string_4)}")