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
    sample_string_1 = "This is a normal line.\nAnother line without the word.\nThis line is critical and important."
    sample_string_2 = "No critical words here. Everything is fine.\nAnother sentence."
    sample_string_3 = "\x80\x90This line contains critical data.\n\x81\x82Another line."
    print(f"Sample 1 result: {check_for_critical(sample_string_1)}")
    print(f"Sample 2 result: {check_for_critical(sample_string_2)}")
    print(f"Sample 3 result: {check_for_critical(sample_string_3)}")