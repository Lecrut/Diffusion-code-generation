import re
def check_for_critical(multi_line_string):
    try:
        lines = multi_line_string.encode('utf-8', errors='ignore').decode('utf-8').splitlines()
    except Exception:
        return False
    pattern = r'critical'
    for line in lines:
        if re.search(pattern, line):
            return True
    return False
if __name__ == '__main__':
    sample_string_1 = "This is a normal line.\nAnother line with critical data.\nFinal line."
    sample_string_2 = "No critical words here.\nAnother test."
    sample_string_3 = "critical error detected\nThis line is fine."
    sample_string_4 = "\x80\x90This line has a critical issue."
    print(f"Sample 1 result: {check_for_critical(sample_string_1)}")
    print(f"Sample 2 result: {check_for_critical(sample_string_2)}")
    print(f"Sample 3 result: {check_for_critical(sample_string_3)}")
    print(f"Sample 4 result: {check_for_critical(sample_string_4)}")