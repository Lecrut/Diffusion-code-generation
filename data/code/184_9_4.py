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
    sample_string1 = "This is a normal line.\nAnother line without the word.\nThis line is critical and important."
    sample_string2 = "No critical issues here.\nEverything is fine."
    sample_string3 = "critical error detected.\nThis line has no issue."
    sample_string4 = "Line with non-utf8 characters: \xff\xfe"
    print(f"Sample 1 contains 'critical': {check_for_critical(sample_string1)}")
    print(f"Sample 2 contains 'critical': {check_for_critical(sample_string2)}")
    print(f"Sample 3 contains 'critical': {check_for_critical(sample_string3)}")
    print(f"Sample 4 contains 'critical': {check_for_critical(sample_string4)}")